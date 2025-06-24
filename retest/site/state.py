import os
import asyncio
import httpx
import requests
import base64
import time
import re
from datetime import datetime, timedelta
import reflex as rx
from dotenv import load_dotenv
from typing import Dict, List, Any, Optional

load_dotenv(dotenv_path="/home/ubuntu/retest/.env")

app = rx.App()


class SpotifyState(rx.State):
    """App state holding current track info."""

    # interval for automatic updates (in seconds)
    update_interval: int = 20
    current_track: str = ""  # e.g. "Song Title – Artist"
    current_cover_url: str = ""  # URL of album art image
    is_fetching: bool = False
    auto_refresh: bool = False
    spotify_access_token: str = ""
    spotify_token_expires_at: int = 0
    is_playing: bool = False
    progress_ms: int = 0
    duration_ms: int = 0
    song_url: str = ""
    artist_url: str = ""

    # Pseudo-timer fields for real-time progress updates
    # Unix timestamp when we last got real data from Spotify
    last_update_time: float = 0.0
    is_pseudo_timer_running: bool = False
    ui_update_trigger: int = 0  # Counter to trigger UI updates

    @rx.var
    def current_progress_ms(self) -> int:
        """Calculate current progress including pseudo-timer offset."""
        # Reference ui_update_trigger to ensure this gets recalculated
        _ = self.ui_update_trigger

        if not self.is_playing or self.last_update_time == 0:
            return self.progress_ms

        current_time = time.time()
        elapsed_seconds = current_time - self.last_update_time
        elapsed_ms = int(elapsed_seconds * 1000)

        # Add elapsed time to the last known progress
        estimated_progress = self.progress_ms + elapsed_ms

        # Don't exceed the track duration
        if self.duration_ms > 0:
            estimated_progress = min(estimated_progress, self.duration_ms)

        # Return the last known progress if too much time has passed (failsafe)
        if elapsed_seconds > 30:  # If more than 30 seconds, something might be wrong
            return self.progress_ms

        return max(0, estimated_progress)  # Ensure non-negative

    @rx.var
    def progress_time_formatted(self) -> str:
        """Format current progress time as MM:SS."""
        progress = self.current_progress_ms  # Use the computed progress
        if progress <= 0:
            return "0:00"
        total_seconds = progress // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    @rx.var
    def duration_time_formatted(self) -> str:
        """Format duration time as MM:SS."""
        if self.duration_ms <= 0:
            return "0:00"
        total_seconds = self.duration_ms // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"

    @rx.var
    def background_image_url(self) -> str:
        """Get background image URL for the Spotify badge."""
        if (
            self.current_cover_url
            and self.current_cover_url != "/placeholder_cover.png"
        ):
            return f"url('{self.current_cover_url}')"
        return "none"

    async def _get_spotify_access_token_from_refresh(self):
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        refresh_token = os.getenv("SPOTIFY_REFRESH_TOKEN")

        if not client_id or not client_secret or not refresh_token:
            print("Error: Spotify credentials not set in environment.")
            return None

        # Check if we have a valid token
        current_time = int(time.time())
        if self.spotify_access_token and current_time < self.spotify_token_expires_at:
            return self.spotify_access_token, self.spotify_token_expires_at

        # Get new token using refresh token
        auth_string = f"{client_id}:{client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

        try:
            response = requests.post(
                "https://accounts.spotify.com/api/token",
                headers=headers,
                data=data,
                timeout=5,
            )
            response.raise_for_status()

            token_data = response.json()
            access_token = token_data["access_token"]

            # Set expiration time (subtract 60 seconds for safety)
            expires_in = token_data.get("expires_in", 3600)
            expires_at = current_time + expires_in - 60

            # Return the token and expiration time for the caller to update state
            return access_token, expires_at

        except Exception as e:
            print(f"Failed to refresh Spotify access token: {e}")
            return None, None

    @rx.event(background=True)
    async def start_spotify_updates(self):
        """Start automatic Spotify updates every 20 seconds (reduced frequency for stability)."""
        async with self:
            if self.auto_refresh:
                return
            self.auto_refresh = True
            self.is_pseudo_timer_running = True

        # Start the pseudo-timer for real-time progress updates
        async def pseudo_timer():
            while True:
                try:
                    async with self:
                        if not self.is_pseudo_timer_running:
                            break
                        # Increment counter to trigger UI updates
                        self.ui_update_trigger += 1
                    # Force UI update every second for smooth progress
                    await asyncio.sleep(1)
                except Exception as e:
                    print(f"Pseudo timer error: {e}")
                    await asyncio.sleep(1)
                    continue

        # Start both timers concurrently
        await asyncio.gather(
            self._spotify_api_loop(), pseudo_timer(), return_exceptions=True
        )

    async def _spotify_api_loop(self):
        """Main Spotify API update loop."""
        while True:
            try:
                async with self:
                    if not self.auto_refresh:
                        break

                # Fetch current track without blocking UI
                await self._fetch_track_background()
                await asyncio.sleep(self.update_interval)
            except Exception as e:
                # Handle any unexpected errors in the background loop
                print(f"Background update error: {e}")
                await asyncio.sleep(self.update_interval)
                continue

    @rx.event
    def stop_spotify_updates(self):
        """Stop automatic Spotify updates."""
        self.auto_refresh = False
        self.is_pseudo_timer_running = False

    async def _fetch_track_background(self):
        """Background track fetching using Spotify API with refresh token."""
        import time

        try:
            token_result = await self._get_spotify_access_token_from_refresh()
            if not token_result or token_result[0] is None:
                return

            access_token, expires_at = token_result

            # Update state with new token within async context
            async with self:
                self.spotify_access_token = access_token
                if isinstance(expires_at, int):
                    self.spotify_token_expires_at = expires_at

            headers = {"Authorization": f"Bearer {access_token}"}

            # Get currently playing track
            response = requests.get(
                "https://api.spotify.com/v1/me/player/currently-playing",
                headers=headers,
                timeout=5,
            )

            # Record the time when we got fresh data
            current_time = time.time()

            if response.status_code == 204:
                # No track currently playing
                try:
                    async with self:
                        self.current_track = "Currently Not Playing"
                        self.current_cover_url = "/placeholder_cover.png"
                        self.is_playing = False
                        self.progress_ms = 0
                        self.duration_ms = 0
                        self.song_url = ""
                        self.artist_url = ""
                        self.last_update_time = current_time
                except:
                    pass
                return

            response.raise_for_status()
            data = response.json()

            if not data.get("item"):
                try:
                    async with self:
                        self.current_track = "No track data"
                        self.current_cover_url = "/placeholder_cover.png"
                        self.is_playing = False
                        self.progress_ms = 0
                        self.duration_ms = 0
                        self.song_url = ""
                        self.artist_url = ""
                        self.last_update_time = current_time
                except:
                    pass
                return

            # Extract track information
            track = data["item"]
            track_name = track.get("name", "")
            artists = track.get("artists", [])
            artist_names = [artist.get("name", "") for artist in artists]
            artist_string = ", ".join(artist_names) if artist_names else ""

            if track_name and artist_string:
                track_display = f"{track_name} – {artist_string}"
            else:
                track_display = track_name or artist_string

            # Get album cover (largest image)
            cover_url = "/placeholder_cover.png"
            images = track.get("album", {}).get("images", [])
            if images:
                cover_url = images[0].get("url", "/placeholder_cover.png")

            # Get additional data
            is_playing = data.get("is_playing", False)
            progress_ms = data.get("progress_ms", 0)
            duration_ms = track.get("duration_ms", 0)
            song_url = track.get("external_urls", {}).get("spotify", "")
            artist_url = ""
            if artists:
                artist_url = artists[0].get("external_urls", {}).get("spotify", "")

            # Update state with better error handling
            try:
                async with self:
                    self.current_track = (
                        track_display if track_display else "Unknown Track"
                    )
                    self.current_cover_url = cover_url
                    self.is_playing = is_playing
                    self.progress_ms = progress_ms
                    self.duration_ms = duration_ms
                    self.song_url = song_url
                    self.artist_url = artist_url
                    self.last_update_time = current_time  # Record when we got this data
            except:
                pass

        except requests.exceptions.RequestException as e:
            if (
                hasattr(e, "response")
                and e.response is not None
                and e.response.status_code == 401
            ):
                # Spotify Token might be expired, clear it to force refresh
                try:
                    async with self:
                        self.spotify_access_token = ""
                        self.spotify_token_expires_at = 0
                except:
                    pass

        except Exception as e:
            pass

    @rx.event
    async def fetch_current_track(self):
        """Manual refresh of current track using Spotify API with refresh token."""
        import time

        if self.is_fetching:
            return

        self.is_fetching = True

        token_result = await self._get_spotify_access_token_from_refresh()
        if not token_result or token_result[0] is None:
            self.is_fetching = False
            return

        access_token, expires_at = token_result

        # Update state with new token
        self.spotify_access_token = access_token
        if isinstance(expires_at, int):
            self.spotify_token_expires_at = expires_at

        headers = {"Authorization": f"Bearer {access_token}"}

        try:
            # Get currently playing track
            response = requests.get(
                "https://api.spotify.com/v1/me/player/currently-playing",
                headers=headers,
                timeout=5,
            )

            # Record the time when we got fresh data
            current_time = time.time()

            if response.status_code == 204:
                # No track currently playing
                self.current_track = "Currently Not Playing"
                self.current_cover_url = "/placeholder_cover.png"
                self.is_playing = False
                self.progress_ms = 0
                self.duration_ms = 0
                self.song_url = ""
                self.artist_url = ""
                self.last_update_time = current_time
                self.is_fetching = False
                return

            response.raise_for_status()
            data = response.json()

            if not data.get("item"):
                self.current_track = "No track data"
                self.current_cover_url = "/placeholder_cover.png"
                self.is_playing = False
                self.progress_ms = 0
                self.duration_ms = 0
                self.song_url = ""
                self.artist_url = ""
                self.last_update_time = current_time
                self.is_fetching = False
                return

            # Extract track information
            track = data["item"]
            track_name = track.get("name", "")
            artists = track.get("artists", [])
            artist_names = [artist.get("name", "") for artist in artists]
            artist_string = ", ".join(artist_names) if artist_names else ""

            if track_name and artist_string:
                track_display = f"{track_name} – {artist_string}"
            else:
                track_display = track_name or artist_string

            # Get album cover (largest image)
            cover_url = "/placeholder_cover.png"
            images = track.get("album", {}).get("images", [])
            if images:
                cover_url = images[0].get("url", "/placeholder_cover.png")

            # Get additional data
            is_playing = data.get("is_playing", False)
            progress_ms = data.get("progress_ms", 0)
            duration_ms = track.get("duration_ms", 0)
            song_url = track.get("external_urls", {}).get("spotify", "")
            artist_url = ""
            if artists:
                artist_url = artists[0].get("external_urls", {}).get("spotify", "")

            self.current_track = track_display if track_display else "Unknown Track"
            self.current_cover_url = cover_url
            self.is_playing = is_playing
            self.progress_ms = progress_ms
            self.duration_ms = duration_ms
            self.song_url = song_url
            self.artist_url = artist_url
            self.last_update_time = current_time  # Record when we got this data

        except requests.exceptions.RequestException as e:
            if (
                hasattr(e, "response")
                and e.response is not None
                and e.response.status_code == 401
            ):
                # Token might be expired, clear it to force refresh
                self.spotify_access_token = ""
                self.spotify_token_expires_at = 0
                print(
                    "Spotify access token expired or invalid, will refresh on next call"
                )
            else:
                print(f"Failed to fetch data from Spotify: {e}")
        except Exception as e:
            print(f"Unexpected error fetching Spotify data: {e}")

        self.is_fetching = False


class SpotifyBadgeState(rx.State):
    """State for managing the Spotify badge visibility."""

    is_expanded: bool = False

    @rx.event
    def toggle_badge(self):
        """Toggle the badge expansion."""
        self.is_expanded = not self.is_expanded

    @rx.event
    def collapse_badge(self):
        """Collapse the badge."""
        self.is_expanded = False

    @rx.event
    def expand_badge(self):
        """Expand the badge."""
        self.is_expanded = True


class GitHubState(rx.State):
    """State for managing GitHub contribution data."""

    # GitHub data
    github_token: str = ""
    github_username: str = "unfortunatelyalex"  # default username
    total_contributions: int = 0
    avatar_url: str = ""
    error_message: str = ""
    is_loading: bool = False
    chart_ready: bool = False  # For rx.skeleton - True when chart is ready to display

    # Contribution data for the chart
    contribution_weeks: List[List[Dict[str, Any]]] = []
    months: List[Dict[str, Any]] = []
    current_year: int = datetime.now().year

    @rx.event
    async def fetch_github_contributions(self, username: Optional[str] = None):
        """Fetch GitHub contribution data using GraphQL API."""
        if self.is_loading:
            return

        self.is_loading = True
        self.chart_ready = False  # Chart is not ready while loading
        self.error_message = ""

        # Use provided username or default
        if username:
            self.github_username = username
        elif not self.github_username:
            self.github_username = "unfortunatelyalex"

        # Get token from environment
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            self.error_message = "GitHub token not found in environment variables"
            self.is_loading = False
            self.chart_ready = False  # Chart not ready due to error
            return

        # Calculate date range for past year
        end_date = datetime.now()
        start_date = end_date - timedelta(days=371)

        # GraphQL query for contribution data
        query = """
        query($username: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $username) {
            contributionsCollection(from: $from, to: $to) {
              totalCommitContributions
              contributionCalendar {
                totalContributions
                weeks {
                  contributionDays {
                    contributionCount
                    date
                    color
                    contributionLevel
                  }
                }
              }
            }
            avatarUrl
          }
        }
        """

        variables = {
            "username": self.github_username,
            "from": start_date.isoformat(),
            "to": end_date.isoformat(),
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                "https://api.github.com/graphql",
                json={"query": query, "variables": variables},
                headers=headers,
                timeout=10,
            )
            response.raise_for_status()

            data = response.json()

            if "errors" in data:
                self.error_message = f"GitHub API error: {data['errors'][0]['message']}"
                self.is_loading = False
                self.chart_ready = False  # Chart not ready due to error
                return

            user_data = data.get("data", {}).get("user")
            if not user_data:
                self.error_message = f"User '{self.github_username}' not found"
                self.is_loading = False
                self.chart_ready = False  # Chart not ready due to error
                return

            # Extract contribution data
            contributions = user_data["contributionsCollection"]
            calendar = contributions["contributionCalendar"]

            self.total_contributions = calendar["totalContributions"]
            self.avatar_url = user_data["avatarUrl"]

            # Process weeks data for the chart
            self.contribution_weeks = []
            for week in calendar["weeks"]:
                week_data = []
                for day in week["contributionDays"]:
                    # Format the tooltip text here during data processing
                    tooltip_text = self.get_formatted_tooltip(
                        day["date"], day["contributionCount"]
                    )
                    week_data.append(
                        {
                            "date": day["date"],
                            "count": day["contributionCount"],
                            "level": self._get_contribution_level(
                                day["contributionCount"]
                            ),
                            "tooltip": tooltip_text,
                            # Keep original API level for reference
                            "api_level": day["contributionLevel"],
                        }
                    )
                self.contribution_weeks.append(week_data)

            # Generate month labels
            self._generate_month_labels()

            # Chart is now ready to display
            self.chart_ready = True

        except requests.exceptions.RequestException as e:
            self.error_message = f"Failed to fetch GitHub data: {str(e)}"
            self.chart_ready = False  # Chart not ready due to error
        except Exception as e:
            self.error_message = f"Unexpected error: {str(e)}"
            self.chart_ready = False  # Chart not ready due to error

        self.is_loading = False

    def _get_contribution_level(self, count: int) -> int:
        """Get contribution level based on count (0-4)."""
        if count == 0:
            return 0  # No contributions
        elif count <= 3:
            return 1  # Low contributions
        elif count <= 6:
            return 2  # Medium contributions
        elif count <= 9:
            return 3  # High contributions
        else:
            return 4  # Very high contributions

    def _generate_month_labels(self):
        """Generate month labels for the GitHub-style contribution chart."""
        from datetime import datetime, timedelta

        self.months = []
        min_weeks_between_labels = 4  # adjust as needed to prevent overlaps

        current_date = datetime.now()
        data_period_start_ref_date = current_date - timedelta(days=366)

        # Chart always starts on Sunday, so get the first Sunday
        chart_start = (
            data_period_start_ref_date
            - timedelta(days=data_period_start_ref_date.weekday() + 1)
            if data_period_start_ref_date.weekday() != 6
            else data_period_start_ref_date
        )

        # For each month in the visible period
        month = chart_start.replace(day=1)
        end_month = current_date.replace(day=1)

        months_tmp = []
        while month <= end_month:
            # Find week index for the 1st of this month
            days_offset = (month - chart_start).days
            week_index = days_offset // 7

            months_tmp.append(
                {
                    "name": month.strftime("%b"),
                    "week_index": week_index,
                }
            )

            # Next month
            if month.month == 12:
                month = month.replace(year=month.year + 1, month=1)
            else:
                month = month.replace(month=month.month + 1)

        # Filter to prevent label overlaps
        filtered_months = []
        last_week = -min_weeks_between_labels
        for month in months_tmp:
            if month["week_index"] - last_week >= min_weeks_between_labels:
                filtered_months.append(month)
                last_week = month["week_index"]

        self.months = filtered_months

    @rx.event
    def set_username(self, username: str):
        """Set the GitHub username."""
        self.github_username = username

    def get_formatted_tooltip(self, date_str: str, count: int) -> str:
        """Get formatted tooltip for a specific date and count."""
        try:
            # Parse date string (YYYY-MM-DD)
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            day_num = dt.day

            # Suffix logic
            if 10 <= day_num % 100 <= 20:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(day_num % 10, "th")

            month = dt.strftime("%B")
            count_str = (
                f"{count} contribution" if count == 1 else f"{count} contributions"
            )

            return f"{count_str} on {month} {day_num}{suffix}"
        except Exception:
            # Fallback format
            return f"{count} contributions on {date_str}"


class TooltipState(rx.State):
    """State for managing tooltips."""

    open_day: str | None = None  # Whether the tooltip is currently open

    @rx.event
    def open_tooltip(self, day_date: str):
        self.open_day = day_date

    @rx.event
    def close_tooltip(self, value: bool, day_date: str):
        if not value and self.open_day == day_date:
            self.open_day = None

    @rx.event
    def close_tt_for_day(self, day_date: str):
        """Close tooltip for a specific day."""
        if self.open_day == day_date:
            self.open_day = None


class DiscordAvatarState(rx.State):
    """State for managing Discord avatar fetching"""

    avatar_url: str = "/profile.jpg"  # Fallback avatar
    user_id: str = os.getenv("DC_UID") or ""
    guild_id: str = os.getenv("DC_GID") or ""
    loading: bool = True  # Loading state for skeleton wrapper

    @rx.event
    async def fetch_discord_avatar(self):
        """Fetch Discord avatar URL from Discord API using bot token"""
        try:
            # Check if required environment variables are set
            if not self.user_id or not self.guild_id:
                print("DC_UID or DC_GID environment variables not found")
                return

            # Get Discord bot token from environment
            discord_token = os.getenv("DC_TOKEN")
            if not discord_token:
                print("DC_TOKEN environment variable not found")
                return

            headers = {
                "Authorization": f"Bot {discord_token}",
                "Content-Type": "application/json",
            }

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://discord.com/api/v10/guilds/{self.guild_id}/members/{self.user_id}",
                    headers=headers,
                )

                if response.status_code == 200:
                    user_data = response.json()
                    avatar_hash = user_data.get("avatar")

                    if avatar_hash:
                        # Construct the full avatar URL
                        self.avatar_url = f"https://cdn.discordapp.com/guilds/{self.guild_id}/users/{self.user_id}/avatars/{avatar_hash}.png?size=4096"
                    else:
                        # User has no custom avatar, use default
                        discriminator = user_data.get("discriminator", "0")
                        if discriminator == "0":  # New username system
                            default_avatar_index = (int(self.user_id) >> 22) % 6
                        else:  # Legacy discriminator system
                            default_avatar_index = int(discriminator) % 5
                        self.avatar_url = f"https://cdn.discordapp.com/embed/avatars/{default_avatar_index}.png"
                else:
                    print(
                        f"Discord API error: {response.status_code} - {response.text}"
                    )

        except Exception as e:
            print(f"Error fetching Discord avatar: {e}")
            # Keep fallback avatar on error
        finally:
            # Always set loading to False when done
            self.loading = False


class ClockState(rx.State):
    """State for the live clock widget."""

    current_time: str = datetime.now().strftime("%H:%M:%S")
    current_date: str = datetime.now().strftime("%B %d, %Y")
    is_running: bool = False

    @rx.event
    def update_time(self):
        """Update the current time."""
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%B %d, %Y")

    @rx.event(background=True)
    async def start_clock(self):
        """Start the live clock updates."""
        async with self:
            if self.is_running:
                return
            self.is_running = True

        while True:
            async with self:
                if not self.is_running:
                    break
                now = datetime.now()
                self.current_time = now.strftime("%H:%M:%S")
                self.current_date = now.strftime("%B %d, %Y")

            await asyncio.sleep(1)  # Update every second

    @rx.event
    def stop_clock(self):
        """Stop the live clock updates."""
        self.is_running = False


class ContactState(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""
    submit_success: bool = False
    name_error: str = ""
    email_error: str = ""
    message_error: str = ""
    is_submitting: bool = False

    @rx.event
    def validate_name(self):
        self.set_name(self.name)  # Ensure the value is set
        if len(self.name.strip()) < 2:
            self.name_error = "Name must be at least 2 characters"
        else:
            self.name_error = ""

    @rx.event
    def validate_email(self):
        self.set_email(self.email)  # Ensure the value is set
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, self.email):
            self.email_error = "Please enter a valid email address"
        else:
            self.email_error = ""

    @rx.event
    def validate_message(self):
        self.set_message(self.message)  # Ensure the value is set
        if len(self.message.strip()) < 10:
            self.message_error = "Message must be at least 10 characters"
        else:
            self.message_error = ""

    @rx.event
    async def send_message(self):
        # Validate all fields
        self.validate_name()
        self.validate_email()
        self.validate_message()

        # Check if there are any errors
        if self.name_error or self.email_error or self.message_error:
            return

        self.is_submitting = True
        yield

        # Simulate API call delay
        await asyncio.sleep(1)

        # Here you'd integrate an email sending service (e.g., SMTP or API call).
        # For now, we simply mark success and print the message server-side.
        print(f"New contact message from {self.name} ({self.email}): {self.message}")

        self.submit_success = True
        self.is_submitting = False

        # Clear form after success
        self.name = ""
        self.email = ""
        self.message = ""

    @rx.event
    def set_name(self, value: str):
        self.name = value
        if self.name_error:  # Clear error when user starts typing
            self.name_error = ""

    @rx.event
    def set_email(self, value: str):
        self.email = value
        if self.email_error:  # Clear error when user starts typing
            self.email_error = ""

    @rx.event
    def set_message(self, value: str):
        self.message = value
        if self.message_error:  # Clear error when user starts typing
            self.message_error = ""

    @rx.event
    def reset_form(self):
        self.submit_success = False
        self.name = ""
        self.email = ""
        self.message = ""
        self.name_error = ""
        self.email_error = ""
        self.message_error = ""
