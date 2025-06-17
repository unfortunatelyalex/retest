# site/pages/blog_post.py
import reflex as rx
from retest.site.components.mobile_nav import mobile_navigation
from retest.site.pages.index import modern_header
from retest.site.state import BlogPostState

# Theme colors (to avoid circular imports)
THEME_COLORS = {
    "light_bg": "#fdf3ea",  # Custom warm cream background
    "dark_bg": "#0a0a0a",   # Deep dark background
}


def blog_post() -> rx.Component:
    """A page to display an individual blog post."""
    return rx.box(
        modern_header(),
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
                # Blog post content
                rx.cond(
                    BlogPostState.post_data == {},
                    # Post not found
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
                            rx.heading(
                                BlogPostState.post_data.get("title", "Blog Post"),
                                size="8",
                                margin_bottom="1rem",
                            ),
                            rx.hstack(
                                rx.text(
                                    BlogPostState.post_data.get("date", ""),
                                    size="3",
                                    color_scheme="gray",
                                ),
                                rx.badge("Blog", variant="soft", color_scheme="blue"),
                                spacing="2",
                                align_items="center",
                            ),
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
        mobile_navigation(),
        on_mount=BlogPostState.fetch_article_identifier_on_load,
        width="100vw",
        min_height="100vh",
        padding="2rem",
        background_color=rx.cond(
            rx.color_mode == "light",
            THEME_COLORS["light_bg"],
            THEME_COLORS["dark_bg"]
        ),
        # style={
        #     "box_sizing": "border_box",
        #     "background": rx.color("gray", 2),  # Add this line
        # }
    )
