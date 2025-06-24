import reflex as rx
from retest.site.blog_parser import blog_parser
from retest.site.models import BlogPost
from retest.site.state import DiscordAvatarState, ClockState
from retest.site.pages.index import modern_header, THEME_COLORS
from typing import List


def back_to_home_button() -> rx.Component:
    """Back to home button with nice styling."""
    return rx.link(
        rx.button(
            rx.icon("arrow-left", size=16),
            "Back to Home",
            variant="soft",
            size="3",
            style={
                "_hover": {
                    "transform": "scale(1.02)",
                    "transition": "transform 0.2s ease-in-out",
                }
            },
        ),
        href="/",
        underline="none",
    )


def blog_post_card(post: BlogPost) -> rx.Component:
    """Individual blog post card component."""
    # Extract slug from file path - handle both full paths and filenames
    from pathlib import Path
    slug = Path(post.file_path).stem if post.file_path else ""
    
    return rx.link(
        rx.card(
            rx.vstack(
                # Header with title and date
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            post.title,
                            size="5",
                            weight="bold",
                            class_name="line-clamp-2",
                        ),
                        rx.text(
                            post.formatted_date,
                            size="2",
                            color="gray",
                            weight="medium",
                        ),
                        align="start",
                        spacing="1",
                        flex="1",
                    ),
                    rx.cond(
                        post.featured,
                        rx.badge(
                            "Featured",
                            color_scheme="gold",
                            variant="soft",
                            size="2",
                        ),
                    ),
                    align="start",
                    justify="between",
                    width="100%",
                ),
                # Description
                rx.text(
                    post.description,
                    size="3",
                    color="gray",
                    class_name="line-clamp-3",
                    line_height="1.6",
                ),
                # Tags
                rx.cond(
                    len(post.tags) > 0,
                    rx.hstack(
                        *[
                            rx.badge(
                                tag,
                                variant="soft",
                                size="1",
                                color_scheme="blue",
                            )
                            for tag in post.tags[:3]  # Show max 3 tags
                        ],
                        spacing="2",
                        wrap="wrap",
                    ),
                ),
                # Footer with author and read more
                rx.hstack(
                    rx.text(
                        f"by {post.author}" if post.author else "",
                        size="2",
                        color="gray",
                        weight="medium",
                    ),
                    rx.spacer(),
                    rx.button(
                        "Read More",
                        rx.icon("arrow-right", size=14),
                        variant="ghost",
                        size="2",
                        style={
                            "_hover": {
                                "background": rx.color("accent", 3),
                            }
                        },
                    ),
                    align="center",
                    width="100%",
                ),
                spacing="4",
                align="start",
                width="100%",
            ),
            size="3",
            style={
                "cursor": "pointer",
                "_hover": {
                    "transform": "translateY(-2px)",
                    "box_shadow": "0 8px 25px rgba(0, 0, 0, 0.15)",
                    "transition": "all 0.2s ease-in-out",
                },
                "transition": "all 0.2s ease-in-out",
                "border": f"1px solid {rx.color('gray', 4)}",
            },
            width="100%",
        ),
        href=f"/blog/{slug}",
        underline="none",
        width="100%",
    )


def blog_header() -> rx.Component:
    """Blog page header with title and navigation."""
    return rx.vstack(
        back_to_home_button(),
        rx.vstack(
            rx.heading(
                "Blog Posts",
                size="8",
                weight="bold",
                text_align="center",
            ),
            rx.text(
                "Thoughts, tutorials, and insights on development",
                size="4",
                color="gray",
                text_align="center",
                weight="medium",
            ),
            spacing="2",
            align="center",
        ),
        spacing="6",
        align="center",
        width="100%",
        margin_bottom="3rem",
    )


def blog_posts_grid(posts: List[BlogPost]) -> rx.Component:
    """Grid layout for blog posts."""
    return rx.cond(
        len(posts) > 0,
        rx.box(
            *[blog_post_card(post) for post in posts],
            display="grid",
            grid_template_columns={
                "base": "1fr",
                "md": "repeat(2, 1fr)",
                "lg": "repeat(3, 1fr)",
            },
            gap="2rem",  # More spacing between cards
            width="100%",
            max_width="100%",  # Prevent overflow
            justify_items="stretch",  # Cards take full width of their cells
            align_items="start",
        ),
        rx.box(
            rx.vstack(
                rx.icon("file-text", size=48, color=rx.color("gray", 8)),
                rx.text(
                    "No blog posts found.",
                    size="5",
                    color="gray",
                    text_align="center",
                    weight="medium",
                ),
                rx.text(
                    "Check back later for new content!",
                    size="3",
                    color="gray",
                    text_align="center",
                ),
                spacing="3",
                align="center",
            ),
        ),
    )


def blog_page() -> rx.Component:
    """Main blog page component."""
    # Load all blog posts
    posts = blog_parser.load_all_posts()

    return rx.box(
        # Main container
        rx.vstack(
            # Modern header (same as index page)
            modern_header(),
            # Blog content
            rx.container(
                rx.vstack(
                    blog_header(),
                    blog_posts_grid(posts),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                max_width="1400px",
                padding_x={"base": "1rem", "sm": "2rem", "lg": "3rem"},
                width="100%",
            ),
            spacing="0",
            width="100%",
            align_items="center",
        ),
        # Page properties
        padding="2rem",
        width="100%",
        max_width="100vw",  # Prevent horizontal overflow
        min_height="100vh",
        overflow_x="hidden",  # Prevent horizontal scroll
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
        style={
            "@keyframes fadeIn": {
                "0%": {"opacity": "0", "transform": "translateY(20px)"},
                "100%": {"opacity": "1", "transform": "translateY(0)"},
            },
            "@keyframes wave": {
                "0%": {"transform": "rotate(0deg)"},
                "100%": {"transform": "rotate(20deg)"},
            },
        },
        # Load states when page mounts
        on_mount=[
            DiscordAvatarState.fetch_discord_avatar,
            ClockState.start_clock,
        ],
    )
