"""Skills page for the portfolio website."""

import reflex as rx
from ..components.layout import page_layout, footer
from ..components.page_nav import page_section, tip_box
from ..components.code import code_block
from ..state import PortfolioState


def skill_category(
    title: str, skills: list, color_scheme: str = "blue"
) -> rx.Component:
    """Skill category component."""
    return rx.box(
        rx.vstack(
            rx.heading(
                title,
                size="5",
                weight="medium",
                color=rx.color("blue", 9),
            ),
            rx.flex(
                rx.foreach(
                    skills,
                    lambda skill: rx.badge(
                        skill,
                        color_scheme="blue",
                        size="2",
                        style={
                            "margin": "0.25rem",
                        },
                    ),
                ),
                wrap="wrap",
                width="100%",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding="1.5rem",
        background_color=rx.color("blue", 2),
        border_radius="12px",
        border=f"1px solid {rx.color('blue', 4)}",
        width="100%",
    )


def skills_page() -> rx.Component:
    """Skills page content."""
    # Define page sections for navigation
    sections = [
        {"id": "overview", "title": "Overview"},
        {"id": "languages", "title": "Languages"},
        {"id": "frameworks", "title": "Frameworks"},
        {"id": "tools", "title": "Tools"},
        {"id": "learning", "title": "Currently Learning"},
    ]

    return page_layout(
        title="Skills",
        description="My technical expertise across programming languages, frameworks, and development tools.",
        sections=sections,
        children=rx.vstack(
            # Overview section
            page_section(
                title="Overview",
                id="overview",
                children=rx.vstack(
                    rx.text(
                        """
                        My technical skill set has been developed through years of hands-on experience, 
                        continuous learning, and working on diverse projects. I believe in choosing the 
                        right tool for the job and staying adaptable to new technologies.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.text(
                        """
                        I'm particularly strong in Python and JavaScript ecosystems, with extensive 
                        experience in full-stack development, DevOps practices, and modern web frameworks.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    tip_box(
                        "I focus on writing clean, maintainable code and following best practices in software development.",
                        type="info",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Skills grid
            rx.vstack(
                # Languages section
                page_section(
                    title="Programming Languages",
                    id="languages",
                    children=skill_category(
                        "Languages", PortfolioState.skills["Languages"], "blue"
                    ),
                ),
                # Frameworks section
                page_section(
                    title="Frameworks & Libraries",
                    id="frameworks",
                    children=skill_category(
                        "Frameworks", PortfolioState.skills["Frameworks"], "green"
                    ),
                ),
                # Tools section
                page_section(
                    title="Tools & Technologies",
                    id="tools",
                    children=skill_category(
                        "Tools", PortfolioState.skills["Tools"], "orange"
                    ),
                ),
                spacing="6",
                width="100%",
            ),
            # Code example section
            page_section(
                title="Code Example",
                id="code-example",
                children=rx.vstack(
                    rx.text(
                        "Here's a sample of my Python code demonstrating clean architecture:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    code_block(
                        """```python
# Example: Clean API endpoint with proper error handling
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

app = FastAPI(title="Portfolio API")

@app.get("/projects", response_model=List[ProjectResponse])
async def get_projects(
    db: Session = Depends(get_database),
    current_user: User = Depends(get_current_user)
) -> List[ProjectResponse]:
    \"\"\"Retrieve all projects for the authenticated user.\"\"\"
    try:
        projects = await project_service.get_user_projects(
            db=db, 
            user_id=current_user.id
        )
        return [ProjectResponse.from_orm(project) for project in projects]
    except Exception as e:
        logger.error(f"Failed to fetch projects: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
```""",
                        language="python",
                        filename="api/projects.py",
                        github_url="https://github.com/username/portfolio-api",
                    ),
                    tip_box(
                        "This example shows proper dependency injection, error handling, and type hints.",
                        type="tip",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Learning section
            page_section(
                title="Currently Learning",
                id="learning",
                children=rx.vstack(
                    rx.text(
                        "I'm always expanding my knowledge. Here's what I'm currently exploring:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.grid(
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "book", size=20, color=rx.color("purple", 9)
                                    ),
                                    rx.heading(
                                        "Machine Learning",
                                        size="4",
                                        color=rx.color("purple", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Exploring TensorFlow and PyTorch for building intelligent applications.",
                                    size="2",
                                    color=rx.color("gray", 11),
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
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "cloud", size=20, color=rx.color("cyan", 9)
                                    ),
                                    rx.heading(
                                        "Cloud Architecture",
                                        size="4",
                                        color=rx.color("cyan", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Diving deeper into serverless computing and microservices architecture.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("cyan", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('cyan', 4)}",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "smartphone", size=20, color=rx.color("pink", 9)
                                    ),
                                    rx.heading(
                                        "Mobile Development",
                                        size="4",
                                        color=rx.color("pink", 9),
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                rx.text(
                                    "Learning React Native and Flutter for cross-platform mobile apps.",
                                    size="2",
                                    color=rx.color("gray", 11),
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("pink", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('pink', 4)}",
                        ),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ),
                    tip_box(
                        "I believe in lifelong learning and regularly allocate time for exploring new technologies.",
                        type="tip",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Collaboration section
            rx.box(
                rx.vstack(
                    rx.heading("Let's Collaborate", size="5", weight="medium"),
                    rx.text(
                        "I'm always excited to work on interesting projects and learn from other developers.",
                        size="3",
                        color=rx.color("gray", 11),
                        text_align="center",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("github", size=18),
                                    rx.text("View My Code"),
                                    spacing="2",
                                    align="center",
                                ),
                                size="3",
                                color_scheme="gray",
                            ),
                            href="https://github.com/username",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("mail", size=18),
                                    rx.text("Get in Touch"),
                                    spacing="2",
                                    align="center",
                                ),
                                size="3",
                                color_scheme="blue",
                            ),
                            href="/contact",
                        ),
                        spacing="3",
                        justify="center",
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
