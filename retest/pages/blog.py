"""Blog page for the portfolio website."""

import reflex as rx
from ..components.layout import page_layout, footer
from ..components.page_nav import page_section, tip_box
from ..state import PortfolioState


def blog_post_card(post: dict) -> rx.Component:
    """Individual blog post card component."""
    return rx.box(
        rx.vstack(
            # Post header
            rx.vstack(
                rx.heading(post["title"], size="5", weight="medium"),
                rx.text(
                    post["excerpt"],
                    size="3",
                    color=rx.color("gray", 10),
                    line_height="1.5",
                ),
                align="start",
                spacing="2",
                width="100%",
            ),
            # Post meta
            rx.hstack(
                rx.text(
                    post["date"],
                    size="2",
                    color=rx.color("gray", 9),
                ),
                rx.text("•", color=rx.color("gray", 8)),
                rx.text(
                    post["read_time"],
                    size="2",
                    color=rx.color("gray", 9),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.foreach(
                        post["tags"],
                        lambda tag: rx.badge(tag, color_scheme="blue", size="1"),
                    ),
                    spacing="1",
                ),
                align="center",
                width="100%",
            ),
            # Read more button
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.text("Read More"),
                        rx.icon("arrow-right", size=16),
                        spacing="2",
                        align="center",
                    ),
                    size="2",
                    variant="soft",
                    color_scheme="blue",
                ),
                href=f"/blog/{post['id']}",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        padding="1.5rem",
        background_color=rx.color("gray", 2),
        border_radius="12px",
        border=f"1px solid {rx.color('gray', 4)}",
        _hover={
            "border_color": rx.color("blue", 6),
            "transform": "translateY(-2px)",
            "box_shadow": f"0 4px 20px {rx.color('gray', 5)}",
            "transition": "all 0.2s ease",
        },
        width="100%",
    )


def blog_page() -> rx.Component:
    """Blog page content."""
    # Define page sections for navigation
    sections = [
        {"id": "overview", "title": "Overview"},
        {"id": "recent", "title": "Recent Posts"},
        {"id": "topics", "title": "Topics I Write About"},
    ]

    return page_layout(
        title="Blog",
        description="Thoughts, tutorials, and insights on software development, technology, and more.",
        sections=sections,
        children=rx.vstack(
            # Overview section
            page_section(
                title="Overview",
                id="overview",
                children=rx.vstack(
                    rx.text(
                        """
                        Welcome to my blog! Here I share my experiences, learnings, and thoughts 
                        about software development, new technologies, and best practices. Whether 
                        you're a fellow developer or just curious about tech, I hope you find 
                        something valuable here.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.text(
                        """
                        I write about real-world problems I've solved, tools I've discovered, 
                        and patterns I've learned. Each post aims to provide practical insights 
                        that you can apply in your own projects.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    tip_box(
                        "Subscribe to my newsletter or follow me on social media to get notified about new posts.",
                        type="info",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Recent posts section
            page_section(
                title="Recent Posts",
                id="recent",
                children=rx.vstack(
                    # Blog posts grid
                    rx.vstack(
                        rx.foreach(
                            PortfolioState.blog_posts,
                            blog_post_card,
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    # View all posts
                    rx.box(
                        rx.vstack(
                            rx.heading("All Posts", size="4", weight="medium"),
                            rx.text(
                                "Browse through all my blog posts by category or chronologically.",
                                size="3",
                                color=rx.color("gray", 11),
                                text_align="center",
                            ),
                            rx.hstack(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("calendar", size=18),
                                        rx.text("By Date"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    size="3",
                                    variant="outline",
                                    color_scheme="blue",
                                ),
                                rx.button(
                                    rx.hstack(
                                        rx.icon("tag", size=18),
                                        rx.text("By Category"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    size="3",
                                    variant="outline",
                                    color_scheme="blue",
                                ),
                                spacing="3",
                            ),
                            spacing="3",
                            align="center",
                            width="100%",
                        ),
                        padding="2rem",
                        background_color=rx.color("gray", 2),
                        border_radius="12px",
                        border=f"1px solid {rx.color('gray', 4)}",
                        text_align="center",
                        margin_top="2rem",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Topics section
            page_section(
                title="Topics I Write About",
                id="topics",
                children=rx.vstack(
                    rx.text(
                        "Here are some of the main topics you'll find on my blog:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Topic categories
                    rx.grid(
                        # Web Development
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "globe", size=20, color=rx.color("blue", 9)
                                    ),
                                    rx.heading(
                                        "Web Development",
                                        size="4",
                                        color=rx.color("blue", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Frontend frameworks, backend architectures, and full-stack development patterns.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                rx.text(
                                    "React, Vue.js, Python, Node.js, APIs",
                                    size="1",
                                    color=rx.color("gray", 10),
                                    font_style="italic",
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("blue", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('blue', 4)}",
                        ),
                        # DevOps
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "settings", size=20, color=rx.color("green", 9)
                                    ),
                                    rx.heading(
                                        "DevOps & Deployment",
                                        size="4",
                                        color=rx.color("green", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Automation, containerization, CI/CD pipelines, and cloud deployment strategies.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                rx.text(
                                    "Docker, Kubernetes, AWS, GitHub Actions",
                                    size="1",
                                    color=rx.color("gray", 10),
                                    font_style="italic",
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("green", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('green', 4)}",
                        ),
                        # Best Practices
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "circle-check",
                                        size=20,
                                        color=rx.color("purple", 9),
                                    ),
                                    rx.heading(
                                        "Best Practices",
                                        size="4",
                                        color=rx.color("purple", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Code quality, testing strategies, architecture patterns, and development workflows.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                rx.text(
                                    "Clean Code, Testing, Architecture, Git",
                                    size="1",
                                    color=rx.color("gray", 10),
                                    font_style="italic",
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("purple", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('purple', 4)}",
                        ),
                        # Tutorials
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "book-open",
                                        size=20,
                                        color=rx.color("orange", 9),
                                    ),
                                    rx.heading(
                                        "Tutorials & Guides",
                                        size="4",
                                        color=rx.color("orange", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Step-by-step tutorials, how-to guides, and practical examples for real projects.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                rx.text(
                                    "How-to, Examples, Walkthroughs",
                                    size="1",
                                    color=rx.color("gray", 10),
                                    font_style="italic",
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("orange", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('orange', 4)}",
                        ),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ),
                    tip_box(
                        "Have a specific topic you'd like me to write about? Feel free to reach out with suggestions!",
                        type="tip",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Newsletter signup section
            rx.box(
                rx.vstack(
                    rx.heading("Stay Updated", size="5", weight="medium"),
                    rx.text(
                        "Get notified when I publish new posts. No spam, just quality content.",
                        size="3",
                        color=rx.color("gray", 11),
                        text_align="center",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="Enter your email",
                            type="email",
                            width="300px",
                        ),
                        rx.button(
                            "Subscribe",
                            size="3",
                            color_scheme="blue",
                        ),
                        spacing="2",
                        justify="center",
                    ),
                    rx.text(
                        "You can unsubscribe at any time.",
                        size="1",
                        color=rx.color("gray", 9),
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                padding="2rem",
                background_color=rx.color("blue", 2),
                border_radius="12px",
                border=f"1px solid {rx.color('blue', 4)}",
                text_align="center",
                margin_top="2rem",
            ),
            # Footer
            footer(),
            spacing="6",
            align="start",
            width="100%",
        ),
    )
