import reflex as rx
from retest.site.components.page_layout import page_layout
from retest.site.state import DiscordAvatarState


def about_intro() -> rx.Component:
    """About me introduction section."""
    return rx.vstack(
        rx.hstack(
            rx.skeleton(
                rx.avatar(
                    fallback="A",
                    src=DiscordAvatarState.avatar_url,
                    size="8",
                    radius="full",
                    style={
                        "border": f"3px solid {rx.color('accent', 6)}",
                        "transition": "transform 0.3s ease",
                        "_hover": {"transform": "scale(1.05)"}
                    }
                ),
                loading=DiscordAvatarState.loading
            ),
            rx.vstack(
                rx.heading(
                    "Alex Rodriguez",
                    size="7",
                    weight="bold",
                    color=rx.color("gray", 12)
                ),
                rx.text(
                    "Full-Stack Developer & Data Enthusiast",
                    size="4",
                    color=rx.color("accent", 11),
                    weight="medium"
                ),
                rx.text(
                    "📍 Based in San Francisco, CA",
                    size="3",
                    color=rx.color("gray", 10)
                ),
                align_items="start",
                spacing="2"
            ),
            align_items="center",
            spacing="6",
            width="100%",
            margin_bottom="8"
        ),
        
        rx.text(
            "I'm a passionate developer with 5+ years of experience building scalable web applications and data-driven solutions. I love exploring the intersection of technology and creativity, always seeking to learn new things and solve complex problems.",
            size="4",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="6"
        ),
        
        align_items="start",
        width="100%",
        id="overview"
    )


def background_section() -> rx.Component:
    """Professional background section."""
    return rx.vstack(
        rx.heading(
            "Background",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="background"
        ),
        
        rx.text(
            "My journey in technology started during my Computer Science studies, where I discovered my passion for both software development and data analysis. Over the years, I've worked on diverse projects ranging from e-commerce platforms to machine learning applications.",
            size="3",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="4"
        ),
        
        rx.text(
            "I specialize in Python ecosystem technologies, with particular expertise in web frameworks like FastAPI, Django, and Reflex. I'm also experienced in frontend development with React and Vue.js, and have a strong background in data science and machine learning.",
            size="3",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="6"
        ),
        
        # Experience timeline
        rx.vstack(
            rx.heading("Experience", size="4", margin_bottom="3"),
            
            rx.vstack(
                # Job 1
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.vstack(
                                rx.text("Senior Full-Stack Developer", weight="bold", size="3"),
                                rx.text("TechCorp Inc.", color=rx.color("accent", 11), size="2"),
                                align_items="start",
                                spacing="1"
                            ),
                            rx.spacer(),
                            rx.text("2022 - Present", size="2", color=rx.color("gray", 10)),
                            align_items="start",
                            width="100%"
                        ),
                        rx.text(
                            "Leading development of scalable web applications and data processing pipelines. Architected microservices handling 1M+ daily requests.",
                            size="2",
                            color=rx.color("gray", 10),
                            line_height="1.6"
                        ),
                        align_items="start",
                        spacing="2"
                    ),
                    size="2",
                    style={"background_color": rx.color("gray", 2, alpha=True)}
                ),
                
                # Job 2
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.vstack(
                                rx.text("Software Developer", weight="bold", size="3"),
                                rx.text("DataFlow Solutions", color=rx.color("accent", 11), size="2"),
                                align_items="start",
                                spacing="1"
                            ),
                            rx.spacer(),
                            rx.text("2020 - 2022", size="2", color=rx.color("gray", 10)),
                            align_items="start",
                            width="100%"
                        ),
                        rx.text(
                            "Developed data analytics platforms and ML models for business intelligence. Improved data processing efficiency by 300%.",
                            size="2",
                            color=rx.color("gray", 10),
                            line_height="1.6"
                        ),
                        align_items="start",
                        spacing="2"
                    ),
                    size="2",
                    style={"background_color": rx.color("gray", 2, alpha=True)}
                ),
                
                spacing="3",
                width="100%"
            ),
            
            align_items="start",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def skills_section() -> rx.Component:
    """Skills and technologies section."""
    return rx.vstack(
        rx.heading(
            "Skills & Technologies",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="skills"
        ),
        
        rx.grid(
            # Frontend
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="monitor", size=20, color=rx.color("blue", 11)),
                        rx.heading("Frontend", size="4"),
                        align_items="center",
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.badge("React", variant="soft", color_scheme="blue"),
                        rx.badge("Vue.js", variant="soft", color_scheme="green"),
                        rx.badge("TypeScript", variant="soft", color_scheme="blue"),
                        rx.badge("Tailwind CSS", variant="soft", color_scheme="cyan"),
                        spacing="2",
                        wrap="wrap"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={"background_color": rx.color("gray", 2, alpha=True)}
            ),
            
            # Backend
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="server", size=20, color=rx.color("green", 11)),
                        rx.heading("Backend", size="4"),
                        align_items="center",
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.badge("Python", variant="soft", color_scheme="green"),
                        rx.badge("FastAPI", variant="soft", color_scheme="red"),
                        rx.badge("Django", variant="soft", color_scheme="green"),
                        rx.badge("PostgreSQL", variant="soft", color_scheme="blue"),
                        spacing="2",
                        wrap="wrap"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={"background_color": rx.color("gray", 2, alpha=True)}
            ),
            
            # Data Science
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="bar-chart", size=20, color=rx.color("purple", 11)),
                        rx.heading("Data Science", size="4"),
                        align_items="center",
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.badge("Pandas", variant="soft", color_scheme="orange"),
                        rx.badge("Scikit-learn", variant="soft", color_scheme="orange"),
                        rx.badge("TensorFlow", variant="soft", color_scheme="orange"),
                        rx.badge("Plotly", variant="soft", color_scheme="blue"),
                        spacing="2",
                        wrap="wrap"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={"background_color": rx.color("gray", 2, alpha=True)}
            ),
            
            # DevOps
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="settings", size=20, color=rx.color("orange", 11)),
                        rx.heading("DevOps", size="4"),
                        align_items="center",
                        spacing="2"
                    ),
                    rx.hstack(
                        rx.badge("Docker", variant="soft", color_scheme="blue"),
                        rx.badge("AWS", variant="soft", color_scheme="orange"),
                        rx.badge("GitHub Actions", variant="soft", color_scheme="gray"),
                        rx.badge("Nginx", variant="soft", color_scheme="green"),
                        spacing="2",
                        wrap="wrap"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={"background_color": rx.color("gray", 2, alpha=True)}
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2"}),
            spacing="4",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def interests_section() -> rx.Component:
    """Personal interests section."""
    return rx.vstack(
        rx.heading(
            "Beyond Code",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="interests"
        ),
        
        rx.text(
            "When I'm not coding, I enjoy exploring the outdoors through hiking and photography. I'm also passionate about music production and have been learning to play the guitar. I love reading about technology trends, contributing to open source projects, and sharing knowledge through blog posts and mentoring.",
            size="3",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="4"
        ),
        
        rx.hstack(
            rx.badge("🎸 Music", variant="soft", color_scheme="purple"),
            rx.badge("📷 Photography", variant="soft", color_scheme="blue"),
            rx.badge("🥾 Hiking", variant="soft", color_scheme="green"),
            rx.badge("📚 Reading", variant="soft", color_scheme="orange"),
            rx.badge("🎯 Mentoring", variant="soft", color_scheme="red"),
            spacing="2",
            wrap="wrap"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def about():
    """About page with personal and professional information."""
    
    # Define sections for "On this page" navigation
    page_sections = [
        {"title": "Overview", "href": "#overview"},
        {"title": "Background", "href": "#background"},
        {"title": "Skills", "href": "#skills"},
        {"title": "Interests", "href": "#interests"}
    ]
    
    # Page content
    content = rx.vstack(
        about_intro(),
        background_section(),
        skills_section(),
        interests_section(),
        spacing="9",
        align_items="start",
        width="100%"
    )
    
    return rx.box(
        page_layout(
            content=content,
            title="About Me",
            on_page_sections=page_sections,
            max_width="4xl"
        ),
        on_mount=[
            DiscordAvatarState.fetch_discord_avatar,
        ]
    )
