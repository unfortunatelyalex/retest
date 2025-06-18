# site/components/spotify_widget.py
import reflex as rx
from retest.site.state import SpotifyState, SpotifyBadgeState


def spotify_collapsed_badge() -> rx.Component:
    """Collapsed state of the Spotify badge - just a small music icon."""
    return rx.box(
        rx.cond(
            (SpotifyState.current_track != "")
            & (SpotifyState.current_track != "Currently Not Playing")
            & (SpotifyState.current_track != "No track data"),
            # Has music - show play/pause indicator
            rx.box(
                rx.cond(
                    SpotifyState.is_playing,
                    rx.hstack(
                        rx.icon("music", size=20, color_scheme="green"),
                        rx.box(
                            width="6px",
                            height="6px",
                            background_color=rx.color("green", 9),
                            border_radius="full",
                            style={"animation": "blink 1.5s infinite"},
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    rx.icon("music", size=20, color_scheme="gray"),
                ),
                padding="12px",
                cursor="pointer",
            ),
            # No music - just music icon
            rx.box(
                rx.icon("music", size=20, color_scheme="gray"),
                padding="12px",
                cursor="pointer",
            ),
        ),
        on_click=SpotifyBadgeState.expand_badge,
        background_color=rx.color("gray", 2),
        border_radius="full",
        style={
            "box_shadow": "0 4px 16px rgba(0,0,0,0.15)",
            "border": "1px solid",
            "border_color": rx.color("gray", 4),
            "backdrop_filter": "blur(10px)",
            "_hover": {
                "transform": "scale(1.05)",
                "box_shadow": "0 6px 20px rgba(0,0,0,0.2)",
            },
        },
    )


def spotify_expanded_badge() -> rx.Component:
    """Expanded state of the Spotify badge - full player interface."""
    return rx.card(
        # Background overlay with blurred album cover
        rx.cond(
            (SpotifyState.current_cover_url != "/placeholder_cover.png")
            & (SpotifyState.current_track != "")
            & (SpotifyState.current_track != "Currently Not Playing")
            & (SpotifyState.current_track != "No track data"),
            rx.box(
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                style={
                    "background_image": SpotifyState.background_image_url,
                    "background_size": "cover",
                    "background_position": "center",
                    "filter": "blur(15px)",
                    "opacity": "0.2",
                    "z_index": "0",
                },
            ),
        ),
        # Main content with higher z-index
        rx.box(
            rx.vstack(
                # Header with controls
                rx.hstack(
                    rx.heading("🎵 Now Playing", size="3"),
                    rx.spacer(),
                    rx.hstack(
                        rx.cond(
                            SpotifyState.auto_refresh,
                            rx.icon_button(
                                rx.icon("pause", size=14),
                                on_click=SpotifyState.stop_spotify_updates,
                                variant="ghost",
                                size="1",
                                aria_label="Stop auto-refresh",
                            ),
                            rx.icon_button(
                                rx.icon("play", size=14),
                                on_click=SpotifyState.start_spotify_updates,
                                variant="ghost",
                                size="1",
                                aria_label="Start auto-refresh",
                            ),
                        ),
                        rx.icon_button(
                            rx.icon("refresh-cw", size=14),
                            on_click=SpotifyState.fetch_current_track,
                            variant="ghost",
                            size="1",
                            aria_label="Refresh",
                            style={
                                "_hover": {
                                    "transform": "rotate(180deg)",
                                    "transition": "transform 0.3s ease",
                                }
                            },
                        ),
                        rx.icon_button(
                            rx.icon("x", size=14),
                            on_click=SpotifyBadgeState.collapse_badge,
                            variant="ghost",
                            size="1",
                            aria_label="Collapse",
                        ),
                        spacing="1",
                    ),
                    align_items="center",
                    width="100%",
                    margin_bottom="0.5rem",
                ),  # Main content area
                rx.cond(
                    (SpotifyState.current_track != "")
                    & (SpotifyState.current_track != "Currently Not Playing")
                    & (SpotifyState.current_track != "No track data"),
                    # Currently playing - compact layout for badge
                    rx.vstack(
                        # Album cover and track info in horizontal layout
                        rx.hstack(
                            # Album cover
                            rx.cond(
                                SpotifyState.current_cover_url
                                != "/placeholder_cover.png",
                                rx.cond(
                                    SpotifyState.song_url != "",
                                    rx.link(
                                        rx.image(
                                            src=SpotifyState.current_cover_url,
                                            width="60px",
                                            height="60px",
                                            border_radius="md",
                                            style={
                                                "box_shadow": "0 4px 12px rgba(0,0,0,0.2)",
                                                "animation": rx.cond(
                                                    SpotifyState.is_playing,
                                                    "pulse 2s infinite",
                                                    "none",
                                                ),
                                            },
                                        ),
                                        href=SpotifyState.song_url,
                                        is_external=True,
                                    ),
                                    rx.image(
                                        src=SpotifyState.current_cover_url,
                                        width="60px",
                                        height="60px",
                                        border_radius="md",
                                        style={
                                            "box_shadow": "0 4px 12px rgba(0,0,0,0.2)",
                                            "animation": rx.cond(
                                                SpotifyState.is_playing,
                                                "pulse 2s infinite",
                                                "none",
                                            ),
                                        },
                                    ),
                                ),
                                rx.box(
                                    rx.icon("music", size=30),
                                    width="60px",
                                    height="60px",
                                    display="flex",
                                    align_items="center",
                                    justify_content="center",
                                    background_color=rx.color("gray", 3),
                                    border_radius="md",
                                ),
                            ),
                            # Track information
                            rx.vstack(
                                rx.cond(
                                    SpotifyState.song_url != "",
                                    rx.link(
                                        SpotifyState.current_track,
                                        href=SpotifyState.song_url,
                                        is_external=True,
                                        weight="bold",
                                        size="3",
                                        text_align="left",
                                        line_height="1.2",
                                        style={
                                            "text_decoration": "none",
                                            "_hover": {"text_decoration": "underline"},
                                            "max_width": "200px",
                                            "white_space": "nowrap",
                                            "overflow": "hidden",
                                            "text_overflow": "ellipsis",
                                        },
                                    ),
                                    rx.text(
                                        SpotifyState.current_track,
                                        weight="bold",
                                        size="3",
                                        text_align="left",
                                        line_height="1.2",
                                        style={
                                            "max_width": "200px",
                                            "white_space": "nowrap",
                                            "overflow": "hidden",
                                            "text_overflow": "ellipsis",
                                        },
                                    ),
                                ),
                                # Play status and time
                                rx.hstack(
                                    rx.cond(
                                        SpotifyState.is_playing,
                                        rx.hstack(
                                            rx.box(
                                                width="6px",
                                                height="6px",
                                                background_color=rx.color("green", 9),
                                                border_radius="full",
                                                style={
                                                    "animation": "blink 1.5s infinite"
                                                },
                                            ),
                                            rx.text(
                                                "Playing",
                                                size="1",
                                                color_scheme="green",
                                            ),
                                            align_items="center",
                                            spacing="2",
                                        ),
                                        rx.hstack(
                                            rx.icon(
                                                "pause", size=12, color_scheme="gray"
                                            ),
                                            rx.text(
                                                "Paused", size="1", color_scheme="gray"
                                            ),
                                            align_items="center",
                                            spacing="1",
                                        ),
                                    ),
                                    rx.text(
                                        f"{SpotifyState.progress_time_formatted} / {SpotifyState.duration_time_formatted}",
                                        size="1",
                                        color_scheme="gray",
                                        style={"font_variant_numeric": "tabular-nums"},
                                    ),
                                    spacing="3",
                                    align_items="center",
                                ),
                                align_items="start",
                                spacing="1",
                                flex="1",
                            ),
                            align_items="center",
                            spacing="3",
                            width="100%",
                        ),
                        # Progress bar
                        rx.cond(
                            SpotifyState.duration_ms > 0,
                            rx.box(
                                rx.box(
                                    width=f"{(SpotifyState.current_progress_ms / SpotifyState.duration_ms) * 100}%",
                                    height="100%",
                                    background_color=rx.color("green", 9),
                                    border_radius="full",
                                    style={
                                        "transition": "width 0.1s ease-out"  # Faster transition for smoother updates
                                    },
                                ),
                                width="100%",
                                height="3px",
                                background_color=rx.color("gray", 4),
                                border_radius="full",
                                overflow="hidden",
                                margin_top="0.5rem",
                            ),
                        ),
                        align_items="start",
                        spacing="2",
                        width="100%",
                    ),
                    # Not listening state - compact
                    rx.vstack(
                        rx.center(
                            rx.box(
                                rx.cond(
                                    SpotifyState.current_track
                                    == "Currently Not Playing",
                                    rx.icon("pause", size=32, color_scheme="gray"),
                                    rx.icon("music", size=32, color_scheme="gray"),
                                ),
                                width="60px",
                                height="60px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                background_color=rx.color("gray", 2),
                                border_radius="md",
                            )
                        ),
                        rx.vstack(
                            rx.cond(
                                SpotifyState.current_track == "Currently Not Playing",
                                rx.text(
                                    "Not playing",
                                    size="3",
                                    weight="medium",
                                    color_scheme="gray",
                                ),
                                rx.text(
                                    "No track data",
                                    size="3",
                                    weight="medium",
                                    color_scheme="gray",
                                ),
                            ),
                            rx.text(
                                "Spotify integration",
                                size="1",
                                color_scheme="gray",
                                text_align="center",
                            ),
                            align_items="center",
                            spacing="1",
                        ),
                        align_items="center",
                        spacing="2",
                        width="100%",
                    ),
                ),
                spacing="0",
                width="100%",
            ),
            position="relative",
            z_index="1",
            width="100%",
        ),
        style={
            "background": rx.color("gray", 1),
            "box_shadow": "0 4px 16px rgba(0,0,0,0.15)",
            "border": "1px solid",
            "border_color": rx.color("gray", 4),
            "backdrop_filter": "blur(10px)",
            "position": "relative",
            "overflow": "hidden",
        },
        size="2",
        width="320px",
    )


def SpotifyWidget():
    """Main Spotify badge widget that can be collapsed or expanded."""
    return rx.box(
        # Desktop version - Fixed positioned badge
        rx.desktop_only(
            rx.box(
                rx.cond(
                    SpotifyBadgeState.is_expanded,
                    spotify_expanded_badge(),
                    spotify_collapsed_badge(),
                ),
                position="fixed",
                bottom="20px",
                right="20px",
                z_index="1000",
                style={"transition": "all 0.3s ease-in-out"},
            )
        ),
        # Mobile version - Drawer from right side
        rx.mobile_and_tablet(
            rx.box(
                rx.cond(
                    SpotifyBadgeState.is_expanded,
                    spotify_expanded_badge(),
                    spotify_collapsed_badge(),
                ),
                position="fixed",
                bottom="20px",
                right="20px",
                z_index="1000",
                style={"transition": "all 0.3s ease-in-out"},
            )
        ),
        # Initialize Spotify updates when component mounts
        on_mount=SpotifyState.start_spotify_updates,
    )
