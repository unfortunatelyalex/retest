# site/pages/blog_post.py
import reflex as rx
from retest.site.components.mobile_nav import mobile_navigation
from retest.site.pages.index import modern_header
from retest.site.state import BlogPostState

# Theme colors (to avoid circular imports)
THEME_COLORS = {
    "light_bg": "#fdf3ea",  # Custom warm cream background
    "dark_bg": "#0a0a0a",  # Deep dark background
}


def blog_post() -> rx.Component:
    """A page to display an individual blog post."""
    return rx.box(
        modern_header(),
        rx.desktop_only(
            rx.container(
                rx.vstack(
                    # Back navigation
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=16),
                            rx.text("Back to Blog"),
                            align_items="center",
                            spacing="2",
                        ),
                        href="/blog",
                        color_scheme="blue",
                        margin_bottom="2rem",
                    ),
                    # Loading state
                    rx.cond(
                        BlogPostState.loading,
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text("Loading post...", size="3"),
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
                        BlogPostState.error_message != "",
                        rx.card(
                            rx.vstack(
                                rx.text("⚠️", font_size="3rem"),
                                rx.heading("Error Loading Post", size="6"),
                                rx.text(
                                    BlogPostState.error_message,
                                    size="3",
                                    color_scheme="red",
                                    text_align="center",
                                ),
                                rx.link(
                                    rx.button("← Back to Blog", variant="outline"),
                                    href="/blog",
                                ),
                                spacing="4",
                                align_items="center",
                                padding="3rem",
                            )
                        ),
                        rx.fragment(),
                    ),
                    # Blog post content
                    rx.cond(
                        (BlogPostState.post_data == {}) & ~BlogPostState.loading & (BlogPostState.error_message == ""),
                        # Post not found (when not loading and no error)
                        rx.card(
                            rx.vstack(
                                rx.text("📄", font_size="3rem"),
                                rx.heading("Post Not Found", size="6"),
                                rx.text(
                                    "The blog post could not be found.",
                                    size="3",
                                    color_scheme="gray",
                                    text_align="center",
                                ),
                                rx.link(
                                    rx.button("← Back to Blog", variant="outline"),
                                    href="/blog",
                                ),
                                spacing="4",
                                align_items="center",
                                padding="3rem",
                            )
                        ),
                        # Post found - render markdown content
                        rx.vstack(
                            # Post header
                            rx.vstack(
                                # Title with featured badge
                                rx.hstack(
                                    rx.heading(
                                        BlogPostState.post_data.get("title", "Blog Post"),
                                        size="8",
                                    ),
                                    rx.cond(
                                        BlogPostState.post_data.get("featured", False),
                                        rx.badge(
                                            "★ Featured",
                                            variant="solid",
                                            color_scheme="yellow",
                                        ),
                                        rx.fragment(),
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    margin_bottom="1rem",
                                ),
                                # Post metadata
                                rx.hstack(
                                    rx.cond(
                                        BlogPostState.post_data.get("last_modified", ""),
                                        rx.text(
                                            BlogPostState.post_data.get("last_modified", ""),
                                            size="3",
                                            color_scheme="gray",
                                        ),
                                        rx.text(
                                            BlogPostState.post_data.get("date", ""),
                                            size="3",
                                            color_scheme="gray",
                                        ),
                                    ),
                                    rx.text("•", size="3", color_scheme="gray"),
                                    rx.text(
                                        f"By {BlogPostState.post_data.get('author', 'Anonymous')}",
                                        size="3",
                                        color_scheme="gray",
                                    ),
                                    rx.text("•", size="3", color_scheme="gray"),
                                    rx.text(
                                        f"{BlogPostState.post_data.get('reading_time', 1)} min read",
                                        size="3",
                                        color_scheme="gray",
                                    ),
                                    spacing="2",
                                    align_items="center",
                                ),
                                # Tags
                                rx.cond(
                                    BlogPostState.post_data.get("tags", []) != [],
                                    rx.hstack(
                                        rx.text("Tags:", size="3", weight="medium"),
                                        rx.badge(
                                            "Blog Post",
                                            variant="soft",
                                            color_scheme="blue",
                                        ),
                                        spacing="2",
                                        align_items="center",
                                        margin_top="0.5rem",
                                    ),
                                    rx.fragment(),
                                ),
                                width="100%",
                                align_items="start",
                                spacing="3",
                                margin_bottom="2rem",
                                padding_bottom="1rem",
                                border_bottom="1px solid var(--gray-a4)",
                            ),
                            # Markdown content
                            rx.box(
                                rx.markdown(BlogPostState.post_data.get("content", "")),
                                width="100%",
                                # style={
                                #     "line_height": "1.7",
                                #     "& h1": {"margin_top": "2rem", "margin_bottom": "1rem"},
                                #     "& h2": {"margin_top": "1.5rem", "margin_bottom": "0.75rem"},
                                #     "& h3": {"margin_top": "1.25rem", "margin_bottom": "0.5rem"},
                                #     "& p": {"margin_bottom": "1rem"},
                                #     "& ul, & ol": {"margin_bottom": "1rem", "padding_left": "1.5rem"},
                                #     "& li": {"margin_bottom": "0.25rem"},
                                #     "& blockquote": {
                                #         "border_left": "4px solid var(--blue-a6)",
                                #         "padding_left": "1rem",
                                #         "margin": "1rem 0",
                                #         "background": "var(--gray-a2)"
                                #     },
                                #     "& code": {
                                #         "background": "var(--gray-a3)",
                                #         "padding": "0.125rem 0.25rem",
                                #         "border_radius": "0.25rem",
                                #         "font_size": "0.875em"
                                #     },
                                #     "& pre": {
                                #         "background": "var(--gray-a3)",
                                #         "padding": "1rem",
                                #         "border_radius": "0.5rem",
                                #         "overflow_x": "auto",
                                #         "margin": "1rem 0"
                                #     }
                                # }
                            ),
                            spacing="4",
                            align_items="start",
                            width="100%",
                        ),
                    ),
                    spacing="4",
                    align_items="start",
                    width="100%",
                    # Extra bottom margin on mobile for nav
                    margin_bottom=["6rem", "6rem", "2rem"],
                ),
                size="3",
                padding="2rem",
            ),
        ),
        rx.mobile_and_tablet(
            rx.container(
                rx.vstack(
                    # Back navigation
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=16),
                            rx.text("Back to Blog"),
                            align_items="center",
                            spacing="2",
                        ),
                        href="/blog",
                        color_scheme="blue",
                        margin_bottom="2rem",
                    ),
                    # Loading state
                    rx.cond(
                        BlogPostState.loading,
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text("Loading post...", size="3"),
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
                        BlogPostState.error_message != "",
                        rx.card(
                            rx.vstack(
                                rx.text("⚠️", font_size="3rem"),
                                rx.heading("Error Loading Post", size="6"),
                                rx.text(
                                    BlogPostState.error_message,
                                    size="3",
                                    color_scheme="red",
                                    text_align="center",
                                ),
                                rx.link(
                                    rx.button("← Back to Blog", variant="outline"),
                                    href="/blog",
                                ),
                                spacing="4",
                                align_items="center",
                                padding="3rem",
                            )
                        ),
                        rx.fragment(),
                    ),
                    # Blog post content
                    rx.cond(
                        (BlogPostState.post_data == {}) & ~BlogPostState.loading & (BlogPostState.error_message == ""),
                        # Post not found (when not loading and no error)
                        rx.card(
                            rx.vstack(
                                rx.text("📄", font_size="3rem"),
                                rx.heading("Post Not Found", size="6"),
                                rx.text(
                                    "The blog post could not be found.",
                                    size="3",
                                    color_scheme="gray",
                                    text_align="center",
                                ),
                                rx.link(
                                    rx.button("← Back to Blog", variant="outline"),
                                    href="/blog",
                                ),
                                spacing="4",
                                align_items="center",
                                padding="3rem",
                            )
                        ),
                        # Post found - render markdown content
                        rx.vstack(
                            # Post header
                            rx.vstack(
                                # Title with featured badge
                                rx.hstack(
                                    rx.heading(
                                        BlogPostState.post_data.get("title", "Blog Post"),
                                        size="8",
                                    ),
                                    rx.cond(
                                        BlogPostState.post_data.get("featured", False),
                                        rx.badge(
                                            "★ Featured",
                                            variant="solid",
                                            color_scheme="yellow",
                                        ),
                                        rx.fragment(),
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    margin_bottom="1rem",
                                ),
                                # Post metadata
                                rx.hstack(
                                    rx.cond(
                                        BlogPostState.post_data.get("last_modified", ""),
                                        rx.text(
                                            BlogPostState.post_data.get("last_modified", ""),
                                            size="3",
                                            color_scheme="gray",
                                        ),
                                        rx.text(
                                            BlogPostState.post_data.get("date", ""),
                                            size="3",
                                            color_scheme="gray",
                                        ),
                                    ),
                                    rx.text("•", size="3", color_scheme="gray"),
                                    rx.text(
                                        f"By {BlogPostState.post_data.get('author', 'Anonymous')}",
                                        size="3",
                                        color_scheme="gray",
                                    ),
                                    rx.text("•", size="3", color_scheme="gray"),
                                    rx.text(
                                        f"{BlogPostState.post_data.get('reading_time', 1)} min read",
                                        size="3",
                                        color_scheme="gray",
                                    ),
                                    spacing="2",
                                    align_items="center",
                                ),
                                # Tags
                                rx.cond(
                                    BlogPostState.post_data.get("tags", []) != [],
                                    rx.hstack(
                                        rx.text("Tags:", size="3", weight="medium"),
                                        rx.badge(
                                            "Blog Post",
                                            variant="soft",
                                            color_scheme="blue",
                                        ),
                                        spacing="2",
                                        align_items="center",
                                        margin_top="0.5rem",
                                    ),
                                    rx.fragment(),
                                ),
                                width="100%",
                                align_items="start",
                                spacing="3",
                                margin_bottom="2rem",
                                padding_bottom="1rem",
                                border_bottom="1px solid var(--gray-a4)",
                            ),
                            # Markdown content
                            rx.box(
                                rx.markdown(BlogPostState.post_data.get("content", "")),
                                width="100%",
                                # style={
                                #     "line_height": "1.7",
                                #     "& h1": {"margin_top": "2rem", "margin_bottom": "1rem"},
                                #     "& h2": {"margin_top": "1.5rem", "margin_bottom": "0.75rem"},
                                #     "& h3": {"margin_top": "1.25rem", "margin_bottom": "0.5rem"},
                                #     "& p": {"margin_bottom": "1rem"},
                                #     "& ul, & ol": {"margin_bottom": "1rem", "padding_left": "1.5rem"},
                                #     "& li": {"margin_bottom": "0.25rem"},
                                #     "& blockquote": {
                                #         "border_left": "4px solid var(--blue-a6)",
                                #         "padding_left": "1rem",
                                #         "margin": "1rem 0",
                                #         "background": "var(--gray-a2)"
                                #     },
                                #     "& code": {
                                #         "background": "var(--gray-a3)",
                                #         "padding": "0.125rem 0.25rem",
                                #         "border_radius": "0.25rem",
                                #         "font_size": "0.875em"
                                #     },
                                #     "& pre": {
                                #         "background": "var(--gray-a3)",
                                #         "padding": "1rem",
                                #         "border_radius": "0.5rem",
                                #         "overflow_x": "auto",
                                #         "margin": "1rem 0"
                                #     }
                                # }
                            ),
                            spacing="4",
                            align_items="start",
                            width="100%",
                        ),
                    ),
                    spacing="4",
                    align_items="start",
                    width="100%",
                    # Extra bottom margin on mobile for nav
                    margin_bottom=["6rem", "6rem", "2rem"],
                ),
                size="2",
                padding="1rem",
            ),
        ),
        mobile_navigation(),
        on_mount=BlogPostState.fetch_article_identifier_on_load,
        width="100vw",
        min_height="100dvh",
        padding="2rem",
        background_color=rx.color_mode_cond(
            light=THEME_COLORS["light_bg"], dark=THEME_COLORS["dark_bg"]
        ),
        # style={
        #     "box_sizing": "border_box",
        #     "background": rx.color("gray", 2),  # Add this line
        # }
    )
