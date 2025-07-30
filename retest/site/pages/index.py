import reflex as rx
from retest.site.components.page_layout import page_layout
from retest.site.components import (
    spotify_widget,
    stats_widget,
    github_widget,
)
from retest.site.state import DiscordAvatarState, ClockState


def introduction_section() -> rx.Component:
    """Introduction section with profile and overview."""
    return rx.vstack(
        # Profile header with avatar and intro
        rx.hstack(
            rx.skeleton(
                rx.avatar(
                    fallback="A", 
                    src=DiscordAvatarState.avatar_url,
                    size="7",
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
                    "Alex's Portfolio",
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
                    "Building innovative web applications and exploring the intersection of technology and creativity.",
                    size="3",
                    color=rx.color("gray", 10),
                    line_height="1.6"
                ),
                align_items="start",
                spacing="2"
            ),
            align_items="center",
            spacing="6",
            width="100%",
            margin_bottom="8"
        ),
        
        # Overview text
        rx.vstack(
            rx.text(
                "Welcome to my digital portfolio! I'm a passionate developer with expertise in Python, web development, and data science. This site showcases my projects, skills, and thoughts on technology.",
                size="3",
                color=rx.color("gray", 11),
                line_height="1.7",
                margin_bottom="4"
            ),
            rx.text(
                "I specialize in building scalable web applications using modern frameworks like Reflex, React, and FastAPI. When I'm not coding, you'll find me exploring new technologies, contributing to open source projects, or sharing knowledge through blog posts.",
                size="3", 
                color=rx.color("gray", 11),
                line_height="1.7",
                margin_bottom="6"
            ),
            align_items="start",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        id="overview"
    )


def quick_stats_section() -> rx.Component:
    """Quick stats and current activity section."""
    return rx.vstack(
        rx.heading(
            "Current Activity", 
            size="5",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="activity"
        ),
        
        # Stats grid
        rx.grid(
            # GitHub Activity Widget
            rx.card(
                github_widget(),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}"
                }
            ),
            
            # Personal Stats Widget  
            rx.card(
                stats_widget.CodingStatsWidget(),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}"
                }
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2"}),
            spacing="4",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def featured_projects_section() -> rx.Component:
    """Featured projects preview section."""
    return rx.vstack(
        rx.heading(
            "Featured Projects",
            size="5", 
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="projects"
        ),
        
        rx.grid(
            # Project cards
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="globe", size=20, color=rx.color("accent", 11)),
                        rx.heading("Portfolio Website", size="3"),
                        align_items="center",
                        spacing="2"
                    ),
                    rx.text(
                        "This very website! Built with Reflex framework, featuring responsive design and modern UI components.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6"
                    ),
                    rx.hstack(
                        rx.badge("Reflex", variant="soft", color_scheme="blue"),
                        rx.badge("Python", variant="soft", color_scheme="green"),
                        rx.badge("Responsive", variant="soft", color_scheme="purple"),
                        spacing="2"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("accent", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="database", size=20, color=rx.color("accent", 11)),
                        rx.heading("Data Analytics Dashboard", size="3"),
                        align_items="center", 
                        spacing="2"
                    ),
                    rx.text(
                        "Interactive dashboard for analyzing large datasets with real-time visualizations and automated reporting.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6"
                    ),
                    rx.hstack(
                        rx.badge("FastAPI", variant="soft", color_scheme="red"),
                        rx.badge("Pandas", variant="soft", color_scheme="orange"), 
                        rx.badge("Plotly", variant="soft", color_scheme="blue"),
                        spacing="2"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("accent", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2"}),
            spacing="4",
            width="100%"
        ),
        
        rx.link(
            rx.button(
                "View All Projects",
                rx.icon(tag="arrow-right", size=16),
                variant="outline",
                size="3",
                style={
                    "margin_top": "1rem",
                    "_hover": {
                        "background_color": rx.color("accent", 3),
                        "border_color": rx.color("accent", 6)
                    }
                }
            ),
            href="/projects"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def get_in_touch_section() -> rx.Component:
    """Get in touch section."""
    return rx.vstack(
        rx.heading(
            "Get in Touch",
            size="5",
            margin_bottom="4", 
            color=rx.color("gray", 12),
            id="contact"
        ),
        
        rx.text(
            "I'm always interested in new opportunities and collaborations. Feel free to reach out if you'd like to work together or just chat about technology!",
            size="3",
            color=rx.color("gray", 10),
            line_height="1.7",
            margin_bottom="4"
        ),
        
        rx.hstack(
            rx.link(
                rx.button(
                    rx.icon(tag="mail", size=16),
                    "Contact Me",
                    variant="solid",
                    size="3"
                ),
                href="/contact"
            ),
            rx.link(
                rx.button(
                    rx.icon(tag="github", size=16),
                    "GitHub",
                    variant="outline", 
                    size="3"
                ),
                href="https://github.com/unfortunatelyalex",
                is_external=True
            ),
            spacing="3"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def index():
    """Main portfolio homepage with OpenAuth-inspired layout."""
    
    # Define sections for "On this page" navigation
    page_sections = [
        {"title": "Overview", "href": "#overview"},
        {"title": "Current Activity", "href": "#activity"}, 
        {"title": "Featured Projects", "href": "#projects"},
        {"title": "Get in Touch", "href": "#contact"}
    ]
    
    # Page content
    content = rx.vstack(
        introduction_section(),
        quick_stats_section(), 
        featured_projects_section(),
        get_in_touch_section(),
        spacing="9",
        align_items="start",
        width="100%"
    )
    
    return rx.box(
        page_layout(
            content=content,
            title="Introduction",
            on_page_sections=page_sections,
            max_width="4xl"
        ),
        
        # Floating Spotify widget (preserved from original)
        spotify_widget.SpotifyWidget(),
        
        # Page initialization
        on_mount=[
            DiscordAvatarState.fetch_discord_avatar,
            ClockState.start_clock,
        ]
    )
