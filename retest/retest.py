import reflex as rx

# Import all pages
from retest.site.pages.index import index
from retest.site.pages.about import about
from retest.site.pages.projects import projects
from retest.site.pages.contact import contact
from retest.site.state import ClockState

# Theme color variables for easy customization
LIGHT_MODE_BG_COLOR = "#fafafa"  # Clean light background
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

# Create app with toast provider
app = rx.App(
    theme=custom_theme, 
    overlay_component=rx.toast.provider()
)

# Add all pages to the app
app.add_page(
    index,
    route="/",
    title="Introduction - Alex's Portfolio",
    on_load=[
        ClockState.start_clock,
    ],
)

app.add_page(
    about,
    route="/about",
    title="About Me - Alex's Portfolio",
)

app.add_page(
    projects,
    route="/projects",
    title="Projects - Alex's Portfolio",
)

app.add_page(
    contact,
    route="/contact",
    title="Contact - Alex's Portfolio",
)
