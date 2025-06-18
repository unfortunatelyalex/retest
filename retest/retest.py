import reflex as rx

# Ensure specific import if * is not intended for all
from retest.site.pages.index import index
from retest.site.pages.blog import blog
from retest.site.pages.blog_post import blog_post
from retest.site.state import SpotifyState, ClockState

# Theme color variables for easy customization
LIGHT_MODE_BG_COLOR = "#fdf3ea"  # Custom warm cream background
DARK_MODE_BG_COLOR = "#0a0a0a"  # Deep dark background
ACCENT_COLOR = "sky"  # Primary accent color
GRAY_COLOR = "slate"  # Gray tone for better contrast


# Utility functions for theme colors (can be imported by components)
def get_theme_background_color(is_light_mode: bool = True) -> str:
    """Get the appropriate background color based on theme mode."""
    return LIGHT_MODE_BG_COLOR if is_light_mode else DARK_MODE_BG_COLOR


def get_all_theme_colors() -> dict:
    """Get all theme colors for easy access."""
    return {
        "light_bg": LIGHT_MODE_BG_COLOR,
        "dark_bg": DARK_MODE_BG_COLOR,
        "accent": ACCENT_COLOR,
        "gray": GRAY_COLOR,
    }


# Define a custom theme with improved contrast and accessibility
custom_theme = rx.theme(
    appearance="inherit",  # System preference for better UX
    has_background=True,
    accent_color=ACCENT_COLOR,
    gray_color=GRAY_COLOR,
    panel_background="solid",
    scaling="100%",
    radius="medium",
)

# Theme configuration with custom colors
# Note: Background color will be applied at the component level for better theme integration

app = rx.App(theme=custom_theme)  # Apply the custom theme

app.add_page(
    index,
    route="/",
    title="Home",
    on_load=[SpotifyState.start_spotify_updates, ClockState.start_clock],
)
app.add_page(blog, route="/blog", title="Blog")
app.add_page(blog_post, route="/blog/[slug]", title="Post")
