# site/pages/blog.py
import reflex as rx
from retest.site.state import BlogState
from retest.site.components.mobile_nav import mobile_navigation
from retest.site.pages.index import modern_header

# Theme colors (to avoid circular imports)
THEME_COLORS = {
    "light_bg": "#fdf3ea",  # Custom warm cream background
    "dark_bg": "#0a0a0a",  # Deep dark background
}


def blog():
    """Blog index page listing all available posts."""
    return rx.box(
        modern_header(),
        rx.container(
            rx.vstack(
                # Back to Home button at the top
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=16),
                            rx.text("Back to Home"),
                            align_items="center",
                            spacing="2",
                        ),
                        href="/",
                        color_scheme="blue",
                        style={"_hover": {"text_decoration": "underline"}},
                    ),
                    rx.spacer(),
                    width="100%",
                    margin_bottom="2rem",
                ),
                rx.vstack(
                    rx.heading("📝 Blog", size="8"),
                    rx.text(
                        "Thoughts, ideas, and tutorials about coding and technology.",
                        size="4",
                        color_scheme="gray",
                        line_height="1.6",
                    ),
                    align_items="center",
                    spacing="3",
                    margin_bottom="3rem",
                ),
                rx.vstack(
                    rx.foreach(
                        BlogState.posts,
                        lambda post: rx.card(
                            rx.vstack(
                                rx.hstack(
                                    rx.vstack(
                                        rx.link(
                                            post["title"],
                                            href=f"/blog/{post['slug']}",
                                            size="5",
                                            weight="bold",
                                            color_scheme="blue",
                                            style={
                                                "_hover": {
                                                    "text_decoration": "underline"
                                                }
                                            },
                                        ),
                                        rx.text(
                                            post.get(
                                                "excerpt",
                                                "Read more about this topic...",
                                            ),
                                            size="3",
                                            color_scheme="gray",
                                            line_height="1.5",
                                            margin_top="0.5rem",
                                        ),
                                        rx.hstack(
                                            rx.text(
                                                post.get("date", ""),
                                                size="2",
                                                color_scheme="gray",
                                            ),
                                            rx.badge(
                                                "Blog",
                                                variant="soft",
                                                size="1",
                                                color_scheme="blue",
                                            ),
                                            align_items="center",
                                            spacing="2",
                                            margin_top="1rem",
                                        ),
                                        align_items="start",
                                        spacing="1",
                                    ),
                                    rx.spacer(),
                                    rx.button(
                                        rx.icon("arrow-right", size=16),
                                        "Read",
                                        on_click=rx.redirect(f"/blog/{post['slug']}"),
                                        variant="outline",
                                        size="2",
                                    ),
                                    align_items="start",
                                    width="100%",
                                ),
                                align_items="start",
                                spacing="3",
                            ),
                            width="100%",
                            style={
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 8px 25px rgba(0,0,0,0.1)",
                                    "transition": "all 0.2s ease",
                                }
                            },
                        ),
                    ),
                    rx.cond(
                        BlogState.posts_count == 0,
                        rx.card(
                            rx.vstack(
                                rx.text("📝", font_size="3rem"),
                                rx.heading("No blog posts found", size="4"),
                                rx.text(
                                    "Add some markdown files to the /public/blog_posts directory to see them here!",
                                    size="3",
                                    color_scheme="gray",
                                    text_align="center",
                                ),
                                spacing="3",
                                align_items="center",
                                padding="2rem",
                            )
                        ),
                        rx.fragment(),
                    ),
                    spacing="4",
                    width="100%",
                ),
                rx.spacer(),
                rx.link(
                    rx.hstack(
                        rx.icon("arrow-left", size=16),
                        rx.text("Back to Home"),
                        align_items="center",
                        spacing="2",
                    ),
                    href="/",
                    color_scheme="blue",
                    margin_top="3rem",
                ),
                spacing="6",
                align_items="center",
                width="100%",
                margin_bottom=[
                    "6rem",
                    "6rem",
                    "2rem",
                ],  # Extra bottom margin on mobile for nav
            ),
            size="3",
            padding="2rem",
        ),
        mobile_navigation(),
        on_mount=BlogState.load_posts,  # Add this line to load posts when page mounts
        width="100vw",
        min_height="100vh",
        padding="2rem",
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
    )
