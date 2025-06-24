"""Individual blog post page component."""

import reflex as rx
from retest.site.blog_parser import blog_parser
from retest.site.models import BlogPost
from retest.site.state import DiscordAvatarState, ClockState
from retest.site.pages.index import modern_header, THEME_COLORS
from typing import Optional


class BlogPostState(rx.State):
    """State for individual blog post page."""
    
    blog_post: Optional[BlogPost] = None
    loading: bool = True
    not_found: bool = False

    @rx.event
    def load_blog_post(self, slug: str):
        """Load a blog post by slug."""
        self.loading = True
        self.not_found = False
        
        try:
            post = blog_parser.get_post_by_slug(slug)
            if post:
                self.blog_post = post
                self.not_found = False
            else:
                self.blog_post = None
                self.not_found = True
        except Exception as e:
            print(f"Error loading blog post: {e}")
            self.blog_post = None
            self.not_found = True
        finally:
            self.loading = False

    @rx.var
    def page_title(self) -> str:
        """Get the page title based on the loaded blog post."""
        if self.blog_post:
            return f"{self.blog_post.title} - Alex's Portfolio"
        return "Blog Post - Alex's Portfolio"
    
    @rx.var
    def current_post(self) -> BlogPost:
        """Get the current blog post, with a fallback if None."""
        if self.blog_post:
            return self.blog_post
        # Return a default BlogPost for type safety
        return BlogPost(
            title="Loading...",
            description="",
            last_modified="",
            tags=[],
            date="",
            content="",
            file_path="",
            tag_display=[],
        )


def back_to_blog_button() -> rx.Component:
    """Back to blog button with nice styling."""
    return rx.link(
        rx.button(
            rx.icon("arrow-left", size=16),
            "Back to Blog",
            variant="soft",
            size="3",
            style={
                "_hover": {
                    "transform": "scale(1.02)",
                    "transition": "transform 0.2s ease-in-out",
                }
            },
        ),
        href="/blog",
        underline="none",
    )


def blog_post_header() -> rx.Component:
    """Header section for individual blog post."""
    return rx.vstack(
        back_to_blog_button(),
        rx.vstack(
            # Featured badge if applicable
            rx.cond(
                BlogPostState.current_post.featured,
                rx.badge(
                    rx.icon("star", size=12),
                    "Featured",
                    color_scheme="yellow",
                    variant="solid",
                    size="2",
                    class_name="flex items-center gap-1",
                ),
            ),
            # Title
            rx.heading(
                BlogPostState.current_post.title,
                size="9",
                weight="bold",
                text_align="center",
                line_height="1.2",
            ),
            # Description
            rx.text(
                BlogPostState.current_post.description,
                size="5",
                color="gray",
                text_align="center",
                weight="medium",
                line_height="1.5",
            ),
            # Meta information
            rx.hstack(
                rx.text(
                    BlogPostState.current_post.formatted_date,
                    size="3",
                    color="gray",
                    weight="medium",
                ),
                rx.cond(
                    BlogPostState.current_post.author != "",
                    rx.fragment(
                        rx.text("•", color="gray", size="3"),
                        rx.text(
                            f"by {BlogPostState.current_post.author}",
                            size="3",
                            color="gray",
                            weight="medium",
                        ),
                    ),
                ),
                spacing="2",
                align="center",
                justify="center",
            ),
            # Tags
            rx.cond(
                BlogPostState.current_post.tags.length() > 0,
                rx.hstack(
                    rx.foreach(
                        BlogPostState.current_post.tags,
                        lambda tag: rx.badge(
                            tag,
                            variant="soft",
                            size="2",
                            color_scheme="blue",
                        ),
                    ),
                    spacing="2",
                    wrap="wrap",
                    justify="center",
                ),
            ),
            spacing="3",
            align="center",
        ),
        spacing="6",
        align="center",
        width="100%",
        margin_bottom="3rem",
    )


def blog_post_content() -> rx.Component:
    """Content section for blog post."""
    return rx.box(
        rx.markdown(
            BlogPostState.current_post.content,
            component_map={
                "h1": lambda text: rx.heading(text, size="8", margin_y="1.5rem"),
                "h2": lambda text: rx.heading(text, size="7", margin_y="1.25rem"),
                "h3": lambda text: rx.heading(text, size="6", margin_y="1rem"),
                "h4": lambda text: rx.heading(text, size="5", margin_y="0.75rem"),
                "h5": lambda text: rx.heading(text, size="4", margin_y="0.5rem"),
                "h6": lambda text: rx.heading(text, size="3", margin_y="0.5rem"),
                "p": lambda text: rx.text(
                    text,
                    size="4",
                    line_height="1.7",
                    margin_y="1rem",
                ),
                "code": lambda text: rx.code(
                    text,
                    color_scheme="gray",
                    size="3",
                ),
                "blockquote": lambda text: rx.box(
                    text,
                    border_left=f"4px solid {rx.color('accent', 8)}",
                    padding_left="1rem",
                    margin_y="1rem",
                    font_style="italic",
                ),
            },
        ),
        max_width="none",
        width="100%",
        style={
            "& img": {
                "max_width": "100%",
                "height": "auto",
                "border_radius": "8px",
                "margin": "1.5rem 0",
            },
            "& table": {
                "width": "100%",
                "border_collapse": "collapse",
                "margin": "1.5rem 0",
            },
            "& th, & td": {
                "border": f"1px solid {rx.color('gray', 6)}",
                "padding": "0.75rem",
                "text_align": "left",
            },
            "& th": {
                "background_color": rx.color("gray", 3),
                "font_weight": "bold",
            },
        },
    )


def blog_post_loading() -> rx.Component:
    """Loading state for blog post."""
    return rx.vstack(
        rx.spinner(size="3"),
        rx.text(
            "Loading blog post...",
            size="4",
            color="gray",
            weight="medium",
        ),
        spacing="4",
        align="center",
        justify="center",
        min_height="50vh",
    )


def blog_post_not_found() -> rx.Component:
    """Not found state for blog post."""
    return rx.vstack(
        back_to_blog_button(),
        rx.vstack(
            rx.icon("file-x", size=64, color=rx.color("gray", 8)),
            rx.heading(
                "Blog Post Not Found",
                size="7",
                color="gray",
                text_align="center",
                weight="bold",
            ),
            rx.text(
                "The blog post you're looking for doesn't exist or has been moved.",
                size="4",
                color="gray",
                text_align="center",
                line_height="1.6",
            ),
            rx.link(
                rx.button(
                    "Browse All Posts",
                    variant="solid",
                    size="3",
                ),
                href="/blog",
                underline="none",
            ),
            spacing="4",
            align="center",
        ),
        spacing="6",
        align="center",
        justify="center",
        min_height="60vh",
    )


def blog_post_page(slug: str = "") -> rx.Component:
    """Individual blog post page component."""
    return rx.box(
        # Main container
        rx.vstack(
            # Modern header (same as other pages)
            modern_header(),
            # Blog post content
            rx.container(
                rx.cond(
                    BlogPostState.loading,
                    blog_post_loading(),
                    rx.cond(
                        BlogPostState.not_found,
                        blog_post_not_found(),
                        rx.cond(
                            BlogPostState.blog_post,
                            rx.vstack(
                                rx.cond(
                                    BlogPostState.blog_post,
                                    blog_post_header(),
                                ),
                                rx.box(
                                    rx.cond(
                                        BlogPostState.blog_post,
                                        blog_post_content(),
                                    ),
                                    max_width="800px",
                                    width="100%",
                                    margin="0 auto",
                                ),
                                spacing="4",
                                align="center",
                                width="100%",
                            ),
                            rx.box(),  # Empty fallback
                        ),
                    ),
                ),
                max_width="1200px",
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
        max_width="100vw",
        min_height="100vh",
        overflow_x="hidden",
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
        # Load blog post when page mounts
        on_mount=[
            DiscordAvatarState.fetch_discord_avatar,
            ClockState.start_clock,
            BlogPostState.load_blog_post(slug),
        ],
    )
