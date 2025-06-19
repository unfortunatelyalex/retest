import reflex as rx
from retest.site.components import (
    spotify_widget,
    blog_widget,
    stats_widget,
    about_contact,
)
from retest.site.components.github_widget import github_widget
from retest.site.state import GitHubState, DiscordAvatarState, ClockState

# Theme colors (to avoid circular imports)
THEME_COLORS = {
    "light_bg": "#fdf3ea",  # Custom warm cream background
    "dark_bg": "#0a0a0a",  # Deep dark background
}


def theme_toggle_button() -> rx.Component:
    return rx.icon_button(
        rx.cond(
            rx.color_mode == "light",
            rx.icon(tag="sun"),
            rx.icon(tag="moon"),
        ),
        on_click=rx.toggle_color_mode,
        radius="full",
        variant="soft",
        size="3",
        aria_label="Toggle theme",
        style={
            "_hover": {
                "transform": "scale(1.1)",
                "transition": "transform 0.2s ease-in-out",
            }
        },
    )


def modern_header() -> rx.Component:
    """Modern centered header at the top of the dashboard"""
    return rx.box(
        # Desktop layout - horizontal with full text
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    # Left side: Avatar and greeting
                    rx.hstack(
                        rx.skeleton(
                            rx.avatar(
                                fallback="A",
                                src=DiscordAvatarState.avatar_url,
                                size="5",
                                radius="full",
                                style={
                                    "transition": "transform 0.3s ease",
                                    "_hover": {"transform": "scale(1.1)"},
                                },
                            ),
                            loading=DiscordAvatarState.loading,
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.heading("Hello, I'm Alex", size="8", weight="bold"),
                                rx.text(
                                    "👋",
                                    font_size="2rem",
                                    style={
                                        "animation": "wave 1s ease-in-out infinite alternate",
                                        "@keyframes wave": {
                                            "0%": {"transform": "rotate(0deg)"},
                                            "100%": {"transform": "rotate(20deg)"},
                                        },
                                    },
                                ),
                                align_items="center",
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.text(
                                    "Welcome to my portfolio dashboard!",
                                    size="5",
                                    color_scheme="gray",
                                ),
                                rx.text("•", color_scheme="gray", size="5"),
                                rx.text(
                                    ClockState.current_time,
                                    size="5",
                                    weight="medium",
                                    color_scheme="blue",
                                    style={
                                        "font_variant_numeric": "tabular-nums",
                                        "letter_spacing": "0.05em",
                                    },
                                ),
                                align_items="center",
                                spacing="3",
                            ),
                            align_items="start",
                            spacing="2",
                        ),
                        align_items="center",
                        spacing="4",
                    ),
                    rx.spacer(),
                    # Right side: Theme toggle and status
                    rx.hstack(
                        rx.cond(
                            ClockState.is_running,
                            rx.badge(
                                "Live", variant="soft", color_scheme="green", size="2"
                            ),
                            rx.badge(
                                "Stopped", variant="soft", color_scheme="gray", size="2"
                            ),
                        ),
                        theme_toggle_button(),
                        align_items="center",
                        spacing="3",
                    ),
                    align_items="center",
                    # width="100%",
                    spacing="4",
                ),
                align_items="center",
                width="100%",
                spacing="3",
            )
        ),
        # Mobile/Tablet layout - compact vertical layout
        rx.mobile_and_tablet(
            rx.vstack(
                # Main content - avatar and greeting
                rx.vstack(
                    rx.hstack(
                        rx.skeleton(
                            rx.avatar(
                                fallback="A",
                                src=DiscordAvatarState.avatar_url,
                                size="4",  # Smaller on mobile
                                radius="full",
                                style={
                                    "transition": "transform 0.3s ease",
                                    "_hover": {"transform": "scale(1.1)"},
                                },
                            ),
                            loading=DiscordAvatarState.loading,
                        ),
                        rx.vstack(
                            rx.hstack(
                                # Smaller heading
                                rx.heading("Hello, I'm Alex", size="6", weight="bold"),
                                rx.text(
                                    "👋",
                                    font_size="1.5rem",  # Smaller wave
                                    style={
                                        "animation": "wave 1s ease-in-out infinite alternate",
                                        "@keyframes wave": {
                                            "0%": {"transform": "rotate(0deg)"},
                                            "100%": {"transform": "rotate(20deg)"},
                                        },
                                    },
                                ),
                                align_items="center",
                                spacing="2",
                            ),
                            rx.text(
                                "Welcome to my portfolio!",  # Shorter text
                                size="3",  # Smaller size
                                color_scheme="gray",
                                text_align="start",
                                style={
                                    "animation": "fadeIn 1s ease-in-out 0.5s both",
                                },
                            ),
                            align_items="start",
                            spacing="1",
                        ),
                        align_items="center",
                        spacing="3",
                    ),
                    # Clock and status in separate row
                    rx.hstack(
                        rx.text(
                            ClockState.current_time,
                            size="4",
                            weight="medium",
                            color_scheme="blue",
                            style={
                                "font_variant_numeric": "tabular-nums",
                                "letter_spacing": "0.05em",
                                "animation": "fadeIn 1s ease-in-out 0.5s both",
                            },
                        ),
                        rx.spacer(),
                        rx.cond(
                            ClockState.is_running,
                            rx.badge(
                                "Live", variant="soft", color_scheme="green", size="1"
                            ),
                            rx.badge(
                                "Stopped", variant="soft", color_scheme="gray", size="1"
                            ),
                        ),
                        theme_toggle_button(),
                        align_items="center",
                        width="100%",
                        spacing="2",
                    ),
                    align_items="start",
                    spacing="3",
                    # width="100%",
                ),
                align_items="center",
                spacing="2",
            )
        ),
        width="100%",
        margin_top="2rem",
        margin_bottom="4rem",
        on_mount=[
            ClockState.start_clock,
            GitHubState.fetch_github_contributions,
            DiscordAvatarState.fetch_discord_avatar,
        ],
    )


def dashboard_card(component: rx.Component, **kwargs) -> rx.Component:
    """Wrapper for consistent card styling across all widgets"""
    return rx.card(
        component,
        style={
            "transition": "transform 0.2s ease, box-shadow 0.2s ease",
            "_hover": {
                "transform": "translateY(-4px)",
                "box_shadow": "0 12px 32px rgba(0,0,0,0.12)",
            },
            "box_shadow": "0 4px 16px rgba(0,0,0,0.06)",
            "border": "1px solid",
            "border_color": rx.color("gray", 4),
            "background": rx.color("gray", 1),
        },
        size="4",
        **kwargs,
    )


def index():
    return rx.box(
        # Main container with viewport dimensions and margins
        rx.vstack(
            # Centered header
            modern_header(),
            # Main dashboard grid - 2x2 layout
            rx.grid(
                # About Me Card
                dashboard_card(
                    about_contact.AboutSection(),
                    grid_column="span 1",
                ),
                # GitHub Activity Card
                dashboard_card(
                    github_widget(),
                    grid_column="span 1",
                ),
                # Coding Stats Card
                dashboard_card(
                    stats_widget.CodingStatsWidget(),
                    grid_column="span 1",
                ),
                # Blog Posts Card
                dashboard_card(
                    blog_widget.BlogPreviewWidget(),
                    grid_column="span 1",
                ),
                # Grid properties - 2x2 layout
                grid_template_columns=rx.breakpoints(
                    {"0px": "1fr", "950px": "repeat(2, 1fr)"}
                ),
                # [
                #     "1fr",  # Mobile: single column
                #     "repeat(2, 1fr)",  # Tablet and up: 2 columns
                # ],
                gap="1.5rem",
                width="88%",
                auto_flow="row",
                align_items="start",
            ),
            # Main stack properties
            spacing="0",
            width="100%",
            height="100%",
            align_items="center",
        ),
        # Spotify badge widget - floating at bottom right
        spotify_widget.SpotifyWidget(),
        # Viewport container properties
        width="100vw",
        height="100vh",
        padding="2rem",
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
        style={
            # "@media (max-width: 768px)": {"padding": "1rem"},
            "@keyframes fadeIn": {
                "0%": {"opacity": "0", "transform": "translateY(20px)"},
                "100%": {"opacity": "1", "transform": "translateY(0)"},
            },
            "@keyframes wave": {
                "0%": {"transform": "rotate(0deg)"},
                "100%": {"transform": "rotate(20deg)"},
            },
            "@keyframes blink": {
                "0%, 50%": {"opacity": "1"},
                "51%, 100%": {"opacity": "0.3"},
            },
            "@keyframes pulse": {
                "0%": {"transform": "scale(1)"},
                "50%": {"transform": "scale(1.05)"},
                "100%": {"transform": "scale(1)"},
            },
        },
    )
