"""Projects page for the portfolio website."""

import reflex as rx
from ..components.layout import page_layout, footer
from ..components.page_nav import page_section, tip_box
from ..state import PortfolioState


def project_card(project: dict) -> rx.Component:
    """Individual project card component."""
    return rx.box(
        rx.vstack(
            # Project header
            rx.hstack(
                rx.vstack(
                    rx.heading(project["name"], size="5", weight="medium"),
                    rx.text(
                        project["description"],
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.5",
                    ),
                    align="start",
                    spacing="1",
                    flex="1",
                ),
                rx.badge(
                    project["status"].replace("-", " ").title(),
                    color_scheme=rx.cond(
                        project["status"] == "completed", "green", "blue"
                    ),
                    size="2",
                ),
                align="start",
                justify="between",
                width="100%",
            ),
            # Tech stack
            rx.vstack(
                rx.text(
                    "Tech Stack",
                    size="2",
                    weight="medium",
                    color=rx.color("gray", 12),
                ),
                rx.text(
                    project["tech_stack"],
                    size="2",
                    color=rx.color("gray", 11),
                ),
                align="start",
                spacing="1",
                width="100%",
            ),
            # Project links
            rx.hstack(
                rx.cond(
                    project["github_url"],
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("github", size=16),
                                rx.text("Code", size="2"),
                                spacing="1",
                                align="center",
                            ),
                            size="2",
                            variant="outline",
                            color_scheme="gray",
                        ),
                        href=project["github_url"],
                        is_external=True,
                    ),
                    rx.fragment(),
                ),
                rx.cond(
                    project["demo_url"],
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon("external-link", size=16),
                                rx.text("Demo", size="2"),
                                spacing="1",
                                align="center",
                            ),
                            size="2",
                            color_scheme="blue",
                        ),
                        href=project["demo_url"],
                        is_external=True,
                    ),
                    rx.fragment(),
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.icon("info", size=16),
                            rx.text("Details", size="2"),
                            spacing="1",
                            align="center",
                        ),
                        size="2",
                        variant="soft",
                        color_scheme="blue",
                    ),
                    href=f"/projects/{project['id']}",
                ),
                spacing="2",
                width="100%",
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


def projects_page() -> rx.Component:
    """Projects page content."""
    # Define page sections for navigation
    sections = [
        {"id": "overview", "title": "Overview"},
        {"id": "featured", "title": "Featured Projects"},
        {"id": "technologies", "title": "Technologies Used"},
    ]

    return page_layout(
        title="Projects",
        description="A showcase of my development work, from web applications to open-source contributions.",
        sections=sections,
        children=rx.vstack(
            # Overview section
            page_section(
                title="Overview",
                id="overview",
                children=rx.vstack(
                    rx.text(
                        """
                        Here's a collection of projects I've built, ranging from personal experiments 
                        to production applications. Each project represents a learning journey and 
                        demonstrates different aspects of my development skills.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.text(
                        """
                        I focus on creating solutions that are not only functional but also maintainable, 
                        scalable, and user-friendly. You'll find detailed documentation, clean code, 
                        and thoughtful architecture in each project.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    tip_box(
                        "Click on any project card to view detailed information, code samples, and live demos.",
                        type="info",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Featured projects section
            page_section(
                title="Featured Projects",
                id="featured",
                children=rx.vstack(
                    # Project grid
                    rx.grid(
                        rx.foreach(
                            PortfolioState.projects,
                            project_card,
                        ),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ),
                    # All projects link
                    rx.box(
                        rx.vstack(
                            rx.heading("More Projects", size="4", weight="medium"),
                            rx.text(
                                "Check out my GitHub for more projects and contributions.",
                                size="3",
                                color=rx.color("gray", 11),
                                text_align="center",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("github", size=18),
                                        rx.text("View All on GitHub"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    size="3",
                                    color_scheme="gray",
                                ),
                                href="https://github.com/username",
                                is_external=True,
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
            # Technologies section
            page_section(
                title="Technologies Used",
                id="technologies",
                children=rx.vstack(
                    rx.text(
                        "Here are some of the key technologies I work with across my projects:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Tech categories
                    rx.grid(
                        # Frontend
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "Frontend", size="4", color=rx.color("blue", 9)
                                ),
                                rx.vstack(
                                    rx.text("• React & Next.js"),
                                    rx.text("• TypeScript"),
                                    rx.text("• Tailwind CSS"),
                                    rx.text("• Vue.js"),
                                    align="start",
                                    spacing="1",
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
                        # Backend
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "Backend", size="4", color=rx.color("green", 9)
                                ),
                                rx.vstack(
                                    rx.text("• Python & FastAPI"),
                                    rx.text("• Node.js & Express"),
                                    rx.text("• PostgreSQL"),
                                    rx.text("• Redis"),
                                    align="start",
                                    spacing="1",
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
                        # DevOps
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "DevOps", size="4", color=rx.color("orange", 9)
                                ),
                                rx.vstack(
                                    rx.text("• Docker & Kubernetes"),
                                    rx.text("• AWS & GCP"),
                                    rx.text("• GitHub Actions"),
                                    rx.text("• Terraform"),
                                    align="start",
                                    spacing="1",
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
                        "I'm always exploring new technologies and adding them to my toolkit based on project needs.",
                        type="tip",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Footer
            footer(),
            spacing="6",
            align="start",
            width="100%",
        ),
    )
