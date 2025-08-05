"""Individual blog post page."""

import reflex as rx
from ..utils.blog import get_blog_post_by_id


class BlogPostState(rx.State):
    """State for handling individual blog post."""

    @rx.var
    def current_post(self) -> dict | None:
        """Get the current blog post based on the post_id URL parameter."""
        # Access the post_id directly - Reflex automatically creates this computed var for dynamic routes
        post_id = self.post_id
        if post_id:
            return get_blog_post_by_id(post_id)
        return None

    @rx.var
    def post_title(self) -> str:
        """Get the title of the current post."""
        post = self.current_post
        return post.get("title", "Post Not Found") if post else "Post Not Found"

    @rx.var
    def post_content(self) -> str:
        """Get the content of the current post."""
        post = self.current_post
        return post.get("content", "") if post else ""

    @rx.var
    def post_excerpt(self) -> str:
        """Get the excerpt of the current post."""
        post = self.current_post
        return post.get("excerpt", "") if post else ""


def blog_post_header(post: dict) -> rx.Component:
    """Blog post header with title, date, tags, etc."""
    return rx.vstack(
        # Title
        rx.heading(
            post["title"],
            size="8",
            weight="bold",
            color=rx.color("gray", 12),
            line_height="1.2",
        ),
        # Meta information
        rx.hstack(
            rx.hstack(
                rx.icon("calendar", size=16),
                rx.text(post["date"], size="2"),
                spacing="1",
                align="center",
                color=rx.color("gray", 9),
            ),
            rx.text("•", color=rx.color("gray", 8)),
            rx.hstack(
                rx.icon("clock", size=16),
                rx.text(post["read_time"], size="2"),
                spacing="1",
                align="center",
                color=rx.color("gray", 9),
            ),
            rx.text("•", color=rx.color("gray", 8)),
            rx.hstack(
                rx.icon("user", size=16),
                rx.text(post["author"], size="2"),
                spacing="1",
                align="center",
                color=rx.color("gray", 9),
            ),
            spacing="2",
            align="center",
        ),
        # Tags
        rx.cond(
            post["tags"],
            rx.hstack(
                rx.foreach(
                    post["tags"],
                    lambda tag: rx.badge(tag, color_scheme="blue", size="1"),
                ),
                spacing="1",
                wrap="wrap",
            ),
            rx.fragment(),
        ),
        # Excerpt/Description
        rx.cond(
            post["excerpt"],
            rx.text(
                post["excerpt"],
                size="4",
                color=rx.color("gray", 11),
                line_height="1.6",
                font_style="italic",
            ),
            rx.fragment(),
        ),
        spacing="4",
        align="start",
        width="100%",
        padding_bottom="2rem",
        border_bottom=f"1px solid {rx.color('gray', 4)}",
        margin_bottom="2rem",
    )


def blog_post_content(content: str) -> rx.Component:
    """Render the blog post content (markdown)."""
    return rx.box(
        rx.markdown(
            content,
            style={
                "& h1": {
                    "font_size": "2rem",
                    "font_weight": "bold",
                    "margin_top": "2rem",
                    "margin_bottom": "1rem",
                    "color": rx.color("gray", 12),
                },
                "& h2": {
                    "font_size": "1.5rem",
                    "font_weight": "600",
                    "margin_top": "1.5rem",
                    "margin_bottom": "0.75rem",
                    "color": rx.color("gray", 12),
                },
                "& h3": {
                    "font_size": "1.25rem",
                    "font_weight": "600",
                    "margin_top": "1.25rem",
                    "margin_bottom": "0.5rem",
                    "color": rx.color("gray", 12),
                },
                "& p": {
                    "line_height": "1.7",
                    "margin_bottom": "1rem",
                    "color": rx.color("gray", 11),
                },
                "& ul, & ol": {
                    "margin_left": "1.5rem",
                    "margin_bottom": "1rem",
                },
                "& li": {
                    "margin_bottom": "0.5rem",
                    "color": rx.color("gray", 11),
                },
                "& code": {
                    "background_color": rx.color("gray", 3),
                    "color": rx.color("iris", 11),
                    "padding": "0.2rem 0.4rem",
                    "border_radius": "4px",
                    "font_size": "0.9rem",
                },
                "& pre": {
                    "background_color": rx.color("gray", 2),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "border_radius": "8px",
                    "padding": "1rem",
                    "overflow_x": "auto",
                    "margin": "1rem 0",
                },
                "& blockquote": {
                    "border_left": f"4px solid {rx.color('iris', 6)}",
                    "padding_left": "1rem",
                    "margin": "1rem 0",
                    "font_style": "italic",
                    "color": rx.color("gray", 10),
                },
                "& a": {
                    "color": rx.color("iris", 11),
                    "text_decoration": "underline",
                },
                "& a:hover": {
                    "color": rx.color("iris", 12),
                },
            },
        ),
        width="100%",
    )


def blog_post_navigation() -> rx.Component:
    """Navigation at the bottom of the blog post."""
    return rx.vstack(
        rx.divider(),
        rx.hstack(
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("arrow-left", size=16),
                        rx.text("Back to Blog"),
                        spacing="2",
                        align="center",
                    ),
                    variant="outline",
                    size="3",
                ),
                href="/blog",
            ),
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon("share", size=16),
                        rx.text("Share"),
                        spacing="2",
                        align="center",
                    ),
                    variant="soft",
                    size="3",
                    color_scheme="blue",
                ),
                href="#",  # Could implement sharing functionality
            ),
            justify="between",
            width="100%",
        ),
        spacing="4",
        margin_top="3rem",
        padding_top="2rem",
    )


def blog_post_page() -> rx.Component:
    """Individual blog post page that loads content dynamically from markdown files."""
    from ..components.layout import layout

    # Use conditional rendering based on whether post exists
    return layout(
        rx.cond(
            BlogPostState.current_post,
            # Post found - render it
            rx.vstack(
                # Page title (dynamic)
                rx.heading(
                    BlogPostState.post_title,
                    size="8",
                    weight="bold",
                    color=rx.color("gray", 12),
                    margin_bottom="1rem",
                ),
                # Page description (dynamic)
                rx.cond(
                    BlogPostState.post_excerpt,
                    rx.text(
                        BlogPostState.post_excerpt,
                        size="4",
                        color=rx.color("gray", 10),
                        margin_bottom="2rem",
                        line_height="1.6",
                    ),
                    rx.fragment(),
                ),
                # Blog post content (inline markdown)
                rx.box(
                    rx.markdown(
                        BlogPostState.post_content,
                        style={
                            "& h1": {
                                "font_size": "2rem",
                                "font_weight": "bold",
                                "margin_top": "2rem",
                                "margin_bottom": "1rem",
                                "color": rx.color("gray", 12),
                            },
                            "& h2": {
                                "font_size": "1.5rem",
                                "font_weight": "600",
                                "margin_top": "1.5rem",
                                "margin_bottom": "0.75rem",
                                "color": rx.color("gray", 12),
                            },
                            "& h3": {
                                "font_size": "1.25rem",
                                "font_weight": "600",
                                "margin_top": "1.25rem",
                                "margin_bottom": "0.5rem",
                                "color": rx.color("gray", 12),
                            },
                            "& p": {
                                "line_height": "1.7",
                                "margin_bottom": "1rem",
                                "color": rx.color("gray", 11),
                            },
                            "& ul, & ol": {
                                "margin_left": "1.5rem",
                                "margin_bottom": "1rem",
                            },
                            "& li": {
                                "margin_bottom": "0.5rem",
                                "color": rx.color("gray", 11),
                            },
                            "& code": {
                                "background_color": rx.color("gray", 3),
                                "color": rx.color("iris", 11),
                                "padding": "0.2rem 0.4rem",
                                "border_radius": "4px",
                                "font_size": "0.9rem",
                            },
                            "& pre": {
                                "background_color": rx.color("gray", 2),
                                "border": f"1px solid {rx.color('gray', 4)}",
                                "border_radius": "8px",
                                "padding": "1rem",
                                "overflow_x": "auto",
                                "margin": "1rem 0",
                            },
                            "& blockquote": {
                                "border_left": f"4px solid {rx.color('iris', 6)}",
                                "padding_left": "1rem",
                                "margin": "1rem 0",
                                "font_style": "italic",
                                "color": rx.color("gray", 10),
                            },
                            "& a": {
                                "color": rx.color("iris", 11),
                                "text_decoration": "underline",
                            },
                            "& a:hover": {
                                "color": rx.color("iris", 12),
                            },
                        },
                    ),
                    width="100%",
                ),
                # Navigation
                blog_post_navigation(),
                spacing="4",
                align="start",
                width="100%",
                max_width="800px",
                margin="0 auto",
            ),
            # Post not found
            rx.vstack(
                rx.heading(
                    "Blog post not found",
                    size="8",
                    weight="bold",
                    color=rx.color("gray", 12),
                ),
                rx.text(
                    "The blog post you're looking for doesn't exist or has been moved.",
                    size="4",
                    color=rx.color("gray", 11),
                    margin_bottom="2rem",
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("arrow-left", size=16),
                            rx.text("Back to Blog"),
                            spacing="2",
                            align="center",
                        ),
                        variant="outline",
                        size="3",
                    ),
                    href="/blog",
                ),
                spacing="4",
                align="center",
                width="100%",
                max_width="600px",
                margin="0 auto",
                text_align="center",
                padding_top="4rem",
            ),
        )
    )
