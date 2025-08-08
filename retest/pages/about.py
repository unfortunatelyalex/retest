"""About Me page for the portfolio website."""

import reflex as rx
from ..components.layout import page_layout, footer
from ..components.page_nav import page_section, tip_box
from ..state import PortfolioState


def about_page() -> rx.Component:
    """About Me page content."""
    # Define page sections for navigation
    sections = [
        {"id": "background", "title": "Background"},
        {"id": "experience", "title": "Experience"},
        {"id": "hobbies", "title": "Hobbies"},
    ]

    content = page_layout(
        title="About Me",
        description="Get to know me, my background, and what drives my passion for development.",
        sections=sections,
        children=rx.vstack(
            # Profile section
            rx.hstack(
                rx.avatar(
                    fallback=PortfolioState.name[0],
                    size="8",
                    radius="full",
                    style={
                        "border": f"3px solid {rx.color('blue', 6)}",
                    },
                ),
                rx.vstack(
                    rx.heading(
                        f"Hello, I'm {PortfolioState.name}",
                        size="6",
                        weight="bold",
                    ),
                    rx.text(
                        PortfolioState.title,
                        size="3",
                        color=rx.color("blue", 9),
                        weight="medium",
                    ),
                    rx.text(
                        PortfolioState.bio,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    align="start",
                    spacing="2",
                ),
                spacing="4",
                align="center",
                width="100%",
                padding="2rem",
                background_color=rx.color("gray", 2),
                border_radius="12px",
                border=f"1px solid {rx.color('gray', 4)}",
            ),
            # Background section
            page_section(
                title="Background",
                id="background",
                children=rx.vstack(
                    rx.text(
                        """
                        I'm a passionate software developer with a strong foundation in modern web technologies 
                        and a love for creating innovative solutions. My journey in technology began with curiosity 
                        about how things work, and has evolved into a comprehensive skill set spanning multiple 
                        programming languages and frameworks.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.text(
                        """
                        I believe in writing clean, maintainable code and staying up-to-date with the latest 
                        industry trends. My approach to development focuses on user experience, performance, 
                        and scalability.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    tip_box(
                        "I'm always eager to learn new technologies and take on challenging projects that push the boundaries of what's possible.",
                        type="tip",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Experience section
            page_section(
                title="Experience",
                id="experience",
                children=rx.vstack(
                    rx.text(
                        "My professional experience spans various domains and technologies:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Experience items
                    rx.vstack(
                        # Experience item 1
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.heading("Senior Software Developer", size="4"),
                                    rx.spacer(),
                                    rx.text(
                                        "2022 - Present",
                                        size="2",
                                        color=rx.color("gray", 10),
                                    ),
                                    width="100%",
                                    align="center",
                                ),
                                rx.text(
                                    "Tech Company Inc.",
                                    size="3",
                                    color=rx.color("blue", 9),
                                    weight="medium",
                                ),
                                rx.unordered_list(
                                    rx.list_item(
                                        "Led development of scalable web applications serving 100k+ users"
                                    ),
                                    rx.list_item(
                                        "Implemented CI/CD pipelines reducing deployment time by 60%"
                                    ),
                                    rx.list_item(
                                        "Mentored junior developers and conducted code reviews"
                                    ),
                                    rx.list_item(
                                        "Architected microservices using Python and Docker"
                                    ),
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("gray", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('gray', 4)}",
                        ),
                        # Experience item 2
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.heading("Full Stack Developer", size="4"),
                                    rx.spacer(),
                                    rx.text(
                                        "2020 - 2022",
                                        size="2",
                                        color=rx.color("gray", 10),
                                    ),
                                    width="100%",
                                    align="center",
                                ),
                                rx.text(
                                    "StartupXYZ",
                                    size="3",
                                    color=rx.color("blue", 9),
                                    weight="medium",
                                ),
                                rx.unordered_list(
                                    rx.list_item(
                                        "Built responsive web applications using React and TypeScript"
                                    ),
                                    rx.list_item(
                                        "Developed RESTful APIs with Python FastAPI"
                                    ),
                                    rx.list_item(
                                        "Collaborated with designers to implement pixel-perfect UIs"
                                    ),
                                    rx.list_item(
                                        "Optimized database queries improving performance by 40%"
                                    ),
                                ),
                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                            padding="1.5rem",
                            background_color=rx.color("gray", 2),
                            border_radius="8px",
                            border=f"1px solid {rx.color('gray', 4)}",
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    tip_box(
                        "For responsive design, I always consider mobile-first approaches and ensure cross-browser compatibility.",
                        type="info",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Hobbies section
            page_section(
                title="Hobbies",
                id="hobbies",
                children=rx.vstack(
                    rx.text(
                        "When I'm not coding, I enjoy:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            "🎸 Playing guitar and exploring different music genres"
                        ),
                        rx.list_item(
                            "📚 Reading tech blogs and staying updated with industry trends"
                        ),
                        rx.list_item("🏃‍♂️ Running and maintaining an active lifestyle"),
                        rx.list_item("🎮 Gaming and exploring virtual worlds"),
                        rx.list_item(
                            "📷 Photography, especially landscape and street photography"
                        ),
                    ),
                    rx.text(
                        """
                        These activities help me maintain creativity and perspective, which I often bring 
                        back into my development work. I believe in work-life balance and the importance 
                        of diverse experiences in shaping problem-solving approaches.
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Contact CTA
            rx.box(
                rx.vstack(
                    rx.heading("Let's Connect", size="5", weight="medium"),
                    rx.text(
                        "I'm always interested in discussing new opportunities and collaborations.",
                        size="3",
                        color=rx.color("gray", 11),
                        text_align="center",
                    ),
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("mail", size=18),
                                rx.text("Get in Touch"),
                                spacing="2",
                                align="center",
                            ),
                            size="3",
                            color_scheme="blue",
                            on_click=rx.redirect("/contact"),
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("download", size=18),
                                rx.text("Download Resume"),
                                spacing="2",
                                align="center",
                            ),
                            size="3",
                            variant="outline",
                            color_scheme="blue",
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
    # Note: on_mount state binding can be wired if needed; relying on layout call above.
    return content
