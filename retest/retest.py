import reflex as rx

# Ensure specific import if * is not intended for all
from retest.site.pages.index import index
from retest.site.pages.blog import blog
from retest.site.pages.blog_post import blog_post
from retest.site.state import SpotifyState, ClockState

# Define a custom theme with improved contrast and accessibility
custom_theme = rx.theme(
    appearance="inherit",  # System preference for better UX
    has_background=True,
    accent_color="sky",
    gray_color="slate",  # Better contrast than mauve
    panel_background="solid",
    scaling="100%",
    radius="medium",
)

app = rx.App(theme=custom_theme)  # Apply the custom theme

app.add_page(
    index,
    route="/",
    title="Home",
    on_load=[SpotifyState.start_spotify_updates, ClockState.start_clock],
)
app.add_page(blog, route="/blog", title="Blog")
app.add_page(blog_post, route="/blog/[slug]", title="Post")
