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
        rx.desktop_only(
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
                        # Loading state
                        rx.cond(
                            BlogState.loading,
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Loading posts...", size="3"),
                                spacing="3",
                                align_items="center",
                                justify_content="center",
                                width="100%",
                                padding="2rem",
                            ),
                            rx.fragment(),
                        ),
                        # Error state
                        rx.cond(
                            BlogState.error_message != "",
                            rx.card(
                                rx.vstack(
                                    rx.text("⚠️", font_size="2rem"),
                                    rx.heading("Error Loading Posts", size="4"),
                                    rx.text(
                                        BlogState.error_message,
                                        size="3",
                                        color_scheme="red",
                                        text_align="center",
                                    ),
                                    spacing="3",
                                    align_items="center",
                                    padding="2rem",
                                )
                            ),
                            rx.fragment(),
                        ),
                        # Blog posts
                        rx.foreach(
                            BlogState.posts,
                            lambda post: rx.card(
                                rx.vstack(
                                    rx.hstack(
                                        rx.vstack(
                                            # Title and featured badge
                                            rx.hstack(
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
                                                rx.cond(
                                                    post.get("featured", False),
                                                    rx.badge(
                                                        "★ Featured",
                                                        variant="solid",
                                                        size="1",
                                                        color_scheme="yellow",
                                                    ),
                                                    rx.fragment(),
                                                ),
                                                align_items="start",
                                                spacing="2",
                                                width="100%",
                                            ),
                                            # Excerpt
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
                                            # Tags - simplified to avoid foreach issues
                                            rx.hstack(
                                                rx.badge(
                                                    "Blog",
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                spacing="1",
                                                margin_top="0.5rem",
                                            ),  # Date, author, and reading time
                                            rx.hstack(
                                                rx.cond(
                                                    post.get("last_modified", ""),
                                                    rx.text(
                                                        post.get("last_modified", ""),
                                                        size="2",
                                                        color_scheme="gray",
                                                    ),
                                                    rx.text(
                                                        post.get("date", ""),
                                                        size="2",
                                                        color_scheme="gray",
                                                    ),
                                                ),
                                                rx.text("•", size="2", color_scheme="gray"),
                                                rx.text(
                                                    f"By {post.get('author', 'Anonymous')}",
                                                    size="2",
                                                    color_scheme="gray",
                                                ),
                                                rx.text("•", size="2", color_scheme="gray"),
                                                rx.text(
                                                    f"{post.get('reading_time', 1)} min read",
                                                    size="2",
                                                    color_scheme="gray",
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
                                        justify_content="space-between",
                                        width="100%",
                                    ),
                                    align_items="start",
                                    spacing="3",
                                ),
                                width="100%",
                            ),
                        ),
                        rx.cond(
                            BlogState.posts_count == 0,
                            rx.box(
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
                                display="flex",
                                justify_content="center",
                                align_items="center",
                                min_height="300px",
                                width="100%",
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
                        margin_top="2rem",
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
        ),
        rx.mobile_and_tablet(
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
                        # Loading state
                        rx.cond(
                            BlogState.loading,
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Loading posts...", size="3"),
                                spacing="3",
                                align_items="center",
                                justify_content="center",
                                width="100%",
                                padding="2rem",
                            ),
                            rx.fragment(),
                        ),
                        # Error state
                        rx.cond(
                            BlogState.error_message != "",
                            rx.card(
                                rx.vstack(
                                    rx.text("⚠️", font_size="2rem"),
                                    rx.heading("Error Loading Posts", size="4"),
                                    rx.text(
                                        BlogState.error_message,
                                        size="3",
                                        color_scheme="red",
                                        text_align="center",
                                    ),
                                    spacing="3",
                                    align_items="center",
                                    padding="2rem",
                                )
                            ),
                            rx.fragment(),
                        ),
                        # Blog posts
                        rx.foreach(
                            BlogState.posts,
                            lambda post: rx.card(
                                rx.vstack(
                                    rx.hstack(
                                        rx.vstack(
                                            # Title and featured badge
                                            rx.hstack(
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
                                                rx.cond(
                                                    post.get("featured", False),
                                                    rx.badge(
                                                        "★ Featured",
                                                        variant="solid",
                                                        size="1",
                                                        color_scheme="yellow",
                                                    ),
                                                    rx.fragment(),
                                                ),
                                                align_items="start",
                                                spacing="2",
                                                width="100%",
                                            ),
                                            # Excerpt
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
                                            # Tags - simplified to avoid foreach issues
                                            rx.hstack(
                                                rx.badge(
                                                    "Blog",
                                                    variant="soft",
                                                    size="1",
                                                    color_scheme="blue",
                                                ),
                                                spacing="1",
                                                margin_top="0.5rem",
                                            ),  # Date, author, and reading time
                                            rx.hstack(
                                                rx.cond(
                                                    post.get("last_modified", ""),
                                                    rx.text(
                                                        post.get("last_modified", ""),
                                                        size="2",
                                                        color_scheme="gray",
                                                    ),
                                                    rx.text(
                                                        post.get("date", ""),
                                                        size="2",
                                                        color_scheme="gray",
                                                    ),
                                                ),
                                                rx.text("•", size="2", color_scheme="gray"),
                                                rx.text(
                                                    f"By {post.get('author', 'Anonymous')}",
                                                    size="2",
                                                    color_scheme="gray",
                                                ),
                                                rx.text("•", size="2", color_scheme="gray"),
                                                rx.text(
                                                    f"{post.get('reading_time', 1)} min read",
                                                    size="2",
                                                    color_scheme="gray",
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
                                        justify_content="space-between",
                                        width="100%",
                                    ),
                                    align_items="start",
                                    spacing="3",
                                ),
                                width="100%",
                            ),
                        ),
                        rx.cond(
                            BlogState.posts_count == 0,
                            rx.box(
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
                                display="flex",
                                justify_content="center",
                                align_items="center",
                                min_height="300px",
                                width="100%",
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
                        margin_top="2rem",
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
                size="2",
                padding="1rem",
            ),
        ),
        mobile_navigation(),
        on_mount=BlogState.load_posts,  # Add this line to load posts when page mounts
        width="100vw",
        min_height="100dvh",
        padding="2rem",
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
    )
