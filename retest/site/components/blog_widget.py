"""Blog widget component for displaying blog posts."""

import reflex as rx
from typing import List
from ..blog_parser import blog_parser
from ..models import BlogPost


class BlogWidgetState(rx.State):
    """State for the blog widget."""

    blog_posts: List[BlogPost] = []
    loading: bool = True
    show_featured_only: bool = False

    @rx.var
    def has_posts(self) -> bool:
        """Check if there are any posts."""
        return len(self.blog_posts) > 0

    @rx.event
    def load_blog_posts(self):
        """Load blog posts from the parser."""
        self.loading = True
        try:
            if self.show_featured_only:
                all_posts = blog_parser.get_featured_posts()
            else:
                all_posts = blog_parser.load_all_posts()

            # Limit to 3 most recent posts for the widget
            self.blog_posts = all_posts[:3]

        except Exception as e:
            print(f"Error loading blog posts: {e}")
            self.blog_posts = []
        finally:
            self.loading = False

    @rx.event
    def toggle_featured_filter(self):
        """Toggle between showing all posts and featured posts only."""
        self.show_featured_only = not self.show_featured_only
        self.load_blog_posts()


def featured_badge() -> rx.Component:
    """Golden featured badge component."""
    return rx.badge(
        rx.icon("star", size=12),
        rx.text("Featured", size="1", weight="medium"),
        color_scheme="yellow",
        variant="solid",
        size="1",
        class_name="flex items-center gap-1",
    )


def blog_post_card(post: BlogPost) -> rx.Component:
    """Individual blog post card component."""
    return rx.box(
        # Desktop layout - more spacious
        rx.desktop_only(
            rx.vstack(
                # Header with title and featured badge
                rx.hstack(
                    rx.heading(
                        post.title,
                        size="4",
                        weight="bold",
                    ),
                    rx.cond(
                        post.featured,
                        featured_badge(),
                        rx.fragment(),
                    ),
                    justify="between",
                    align="start",
                    width="100%",
                    spacing="2",
                ),
                # Description
                rx.text(
                    post.description,
                    size="2",
                    color=rx.color("gray", 11),
                    line_height="1.5",
                ),
                # Tags
                rx.cond(
                    post.tag_display != "",
                    rx.hstack(
                        rx.text(
                            "Tags: ",
                            size="1",
                            color=rx.color("blue", 9),
                            # move the text down by 1px
                            style={"marginTop": "1px"},
                        ),
                        rx.foreach(
                            post.tag_display,
                            lambda tag: rx.badge(
                                tag,
                                size="1",
                                color_scheme="blue",
                                variant="soft",
                            ),
                        ),
                    ),
                    rx.fragment(),
                ),
                # Footer with author and date
                rx.hstack(
                    rx.cond(
                        post.author != "",
                        rx.text(
                            f"By {post.author}",
                            size="1",
                            color=rx.color("gray", 10),
                        ),
                        rx.fragment(),
                    ),
                    rx.spacer(),
                    rx.text(
                        post.formatted_date,
                        size="2",
                        color="gray",
                        weight="medium",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
        ),
        # Mobile/tablet layout - more compact
        rx.mobile_and_tablet(
            rx.vstack(
                # Header with title and featured badge (stacked on mobile)
                rx.vstack(
                    rx.hstack(
                        rx.heading(
                            post.title,
                            size="3",
                            weight="bold",
                        ),
                        rx.cond(
                            post.featured,
                            featured_badge(),
                            rx.fragment(),
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        spacing="2",
                    ),
                    spacing="2",
                    width="100%",
                ),
                # Description (smaller on mobile)
                rx.text(
                    post.description,
                    size="1",
                    color=rx.color("gray", 11),
                    line_height="1.4",
                ),
                # Tags (smaller)
                rx.cond(
                    post.tag_display != "",
                    rx.hstack(
                        rx.text(
                            "Tags: ",
                            size="1",
                            color=rx.color("blue", 9),
                            # move the text down by 1px
                            style={"marginTop": "1px"},
                        ),
                        rx.foreach(
                            post.tag_display,
                            lambda tag: rx.badge(
                                tag,
                                size="1",
                                color_scheme="blue",
                                variant="soft",
                            ),
                        ),
                    ),
                    rx.fragment(),
                ),
                # Footer (stacked on mobile for better readability)
                rx.vstack(
                    rx.cond(
                        post.author != "",
                        rx.text(
                            f"By {post.author}",
                            size="1",
                            color=rx.color("gray", 10),
                        ),
                        rx.fragment(),
                    ),
                    rx.text(
                        post.formatted_date,
                        size="2",
                        color="gray",
                        weight="medium",
                    ),
                    spacing="1",
                    align="start",
                    width="100%",
                ),
                spacing="2",
                align="start",
                width="100%",
            ),
        ),
        width="100%",
        padding_y="12px",
        border_bottom=f"1px solid {rx.color('gray', 6)}",
    )


def blog_widget_loading() -> rx.Component:
    """Loading state for the blog widget."""
    return rx.center(
        rx.vstack(
            rx.spinner(size="3"),
            rx.text("Loading blog posts...", size="2", color=rx.color("gray", 11)),
            spacing="3",
            align="center",
        ),
        height="200px",
        width="100%",
    )


def blog_widget_empty() -> rx.Component:
    """Empty state for the blog widget."""
    return rx.center(
        rx.vstack(
            rx.icon("file-text", size=32, color=rx.color("gray", 8)),
            rx.text(
                "No blog posts found",
                size="3",
                weight="medium",
                color=rx.color("gray", 11),
            ),
            rx.text(
                "Check back later for new content!",
                size="2",
                color=rx.color("gray", 10),
            ),
            spacing="2",
            align="center",
        ),
        height="200px",
        width="100%",
    )


def blog_widget() -> rx.Component:
    """Main blog widget component."""
    return rx.box(
        # Desktop layout
        rx.desktop_only(
            rx.flex(
                # Header section
                rx.flex(
                    rx.hstack(
                        rx.icon("book-open", size=20),
                        rx.heading("Latest Blog Posts", size="5", weight="bold"),
                        align="center",
                        spacing="2",
                    ),
                    rx.button(
                        rx.cond(
                            BlogWidgetState.show_featured_only,
                            "Show All",
                            "Featured Only",
                        ),
                        rx.icon("filter", size=14),
                        size="2",
                        variant="outline",
                        on_click=BlogWidgetState.toggle_featured_filter,
                    ),
                    rx.link(
                        rx.button(
                            "View All Blog Posts",
                            rx.icon("arrow-right", size=14),
                            size="2",
                            variant="soft",
                        ),
                        href="/blog",
                        underline="none",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    margin_bottom="16px",
                ),
                direction="column",
                width="100%",
            )
        ),
        # Mobile/tablet layout
        rx.mobile_and_tablet(
            rx.flex(
                # Header section
                rx.flex(
                    rx.hstack(
                        rx.icon("book-open", size=18),
                        rx.heading("Latest Blog Posts", size="4", weight="bold"),
                        align="center",
                        spacing="2",
                    ),
                    rx.button(
                        rx.cond(
                            BlogWidgetState.show_featured_only,
                            "Show All",
                            "Featured Only",
                        ),
                        rx.icon("filter", size=12),
                        size="1",
                        variant="outline",
                        on_click=BlogWidgetState.toggle_featured_filter,
                        width="100%",
                    ),
                    rx.link(
                        rx.button(
                            "View All Blog Posts",
                            rx.icon("arrow-right", size=12),
                            size="1",
                            variant="soft",
                            width="100%",
                        ),
                        href="/blog",
                        underline="none",
                        width="100%",
                    ),
                    direction="column",
                    spacing="3",
                    width="100%",
                    margin_bottom="12px",
                ),
                direction="column",
                width="100%",
            )
        ),
        # Divider
        rx.divider(margin_bottom="16px"),
        # Content area - blog posts
        rx.cond(
            BlogWidgetState.loading,
            blog_widget_loading(),
            rx.cond(
                ~BlogWidgetState.has_posts,
                blog_widget_empty(),
                rx.vstack(
                    rx.foreach(
                        BlogWidgetState.blog_posts,
                        blog_post_card,
                    ),
                    spacing="0",  # No spacing since cards have borders
                    width="100%",
                ),
            ),
        ),
        width="100%",
        on_mount=BlogWidgetState.load_blog_posts,
    )
