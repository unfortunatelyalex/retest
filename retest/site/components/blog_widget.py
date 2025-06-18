# site/components/blog_widget.py
import reflex as rx
from retest.site.state import BlogState


# Keep the old POSTS for backward compatibility, but make it dynamic
POSTS = [
    {
        "slug": "hello-world",
        "title": "Hello World",
        "date": "June 10, 2025",
        "excerpt": "My first blog post about getting started with Reflex and web development.",
        "tags": ["Intro", "Reflex"],
        "body": "# Hello World\n\nWelcome to my blog!",
    },
    {
        "slug": "reflex-tips",
        "title": "Building Apps with Reflex",
        "date": "May 5, 2025",
        "excerpt": "Essential tips and tricks for building modern web applications with Reflex.",
        "tags": ["Tutorial", "Reflex"],
        "body": "# Building Apps with Reflex\n\nHere are some great tips for building with Reflex...",
    },
]


def BlogPreviewWidget():
    return rx.vstack(
        rx.hstack(
            rx.heading("📜 Latest Posts", size="3", margin_bottom="0.25em"),
            rx.spacer(),
            rx.link(
                rx.icon_button(
                    rx.icon("external-link", size=14),
                    variant="ghost",
                    size="2",
                    aria_label="View all posts",
                ),
                href="/blog",
            ),
            align_items="center",
            width="100%",
        ),
        rx.vstack(
            rx.foreach(
                BlogState.preview_posts,
                lambda post: rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.link(
                                post["title"],
                                href=f"/blog/{post['slug']}",
                                weight="medium",
                                color_scheme="blue",
                                style={"_hover": {"text_decoration": "underline"}},
                            ),
                            rx.spacer(),
                            rx.text(
                                post.get("date", ""), size="1", color_scheme="gray"
                            ),
                            align_items="center",
                            width="100%",
                        ),
                        rx.text(
                            post.get("excerpt", ""),
                            size="2",
                            color_scheme="gray",
                            line_height="1.4",
                        ),
                        rx.text("Tags: Blog", size="1", color_scheme="gray"),
                        align_items="start",
                        spacing="1",
                        padding="0.5rem",
                        border_radius="md",
                        style={
                            "_hover": {
                                "background_color": rx.color("gray", 2),
                                "transition": "background-color 0.2s ease",
                            }
                        },
                    ),
                    width="100%",
                ),
            ),
            rx.cond(
                BlogState.preview_posts.length() == 0,
                rx.text("No blog posts available.", size="2", color_scheme="gray"),
                rx.fragment(),
            ),
            spacing="2",
            width="100%",
        ),
        rx.cond(
            BlogState.has_more_posts,
            rx.link(
                rx.hstack(
                    rx.text("View all posts", size="2"),
                    rx.icon("arrow-right", size=14),
                    align_items="center",
                    spacing="1",
                ),
                href="/blog",
                color_scheme="blue",
                margin_top="0.5rem",
            ),
            rx.cond(
                BlogState.preview_posts.length() > 0,
                rx.text(
                    f"All {BlogState.preview_posts.length()} posts shown",
                    size="1",
                    color_scheme="gray",
                    margin_top="0.5rem",
                ),
                rx.fragment(),
            ),
        ),
        align_items="start",
        spacing="2",  # Reduced spacing
        padding="1rem",  # Added explicit padding
        width="100%",
        height="auto",  # Let content determine height
        on_mount=BlogState.load_posts,  # Load posts when widget mounts
    )
