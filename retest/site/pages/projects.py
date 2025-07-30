import reflex as rx
from retest.site.components.page_layout import page_layout


def project_card(
    title: str,
    description: str,
    technologies: list[str],
    github_url: str | None = None,
    demo_url: str | None = None,
    icon: str = "folder"
) -> rx.Component:
    """Create a project card component."""
    return rx.card(
        rx.vstack(
            # Header with icon and title
            rx.hstack(
                rx.icon(tag=icon, size=24, color=rx.color("accent", 11)),
                rx.heading(title, size="4", weight="bold"),
                align_items="center",
                spacing="3"
            ),
            
            # Description
            rx.text(
                description,
                size="3",
                color=rx.color("gray", 10),
                line_height="1.6",
                margin_bottom="4"
            ),
            
            # Technologies
            rx.hstack(
                *[
                    rx.badge(tech, variant="soft", color_scheme="blue")
                    for tech in technologies
                ],
                spacing="2",
                margin_bottom="4",
                wrap="wrap"
            ),
            
            # Action buttons
            rx.hstack(
                rx.cond(
                    github_url is not None,
                    rx.link(
                        rx.button(
                            rx.icon(tag="github", size=16),
                            "Code",
                            variant="outline",
                            size="2"
                        ),
                        href=github_url or "",
                        is_external=True
                    ),
                    rx.spacer()
                ),
                rx.cond(
                    demo_url is not None,
                    rx.link(
                        rx.button(
                            rx.icon(tag="external-link", size=16),
                            "Demo",
                            variant="solid",
                            size="2"
                        ),
                        href=demo_url or "",
                        is_external=True
                    ),
                    rx.spacer()
                ),
                spacing="2"
            ),
            
            align_items="start",
            spacing="3",
            width="100%"
        ),
        size="4",
        style={
            "background_color": rx.color("gray", 2, alpha=True),
            "border": f"1px solid {rx.color('gray', 4)}",
            "_hover": {
                "border_color": rx.color("accent", 6),
                "transform": "translateY(-2px)",
                "transition": "all 0.2s ease"
            }
        }
    )


def projects_overview() -> rx.Component:
    """Projects overview section."""
    return rx.vstack(
        rx.text(
            "Here's a collection of projects I've built, ranging from web applications to data science experiments. Each project represents a learning journey and demonstrates different aspects of my technical skills.",
            size="4",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="6"
        ),
        align_items="start",
        width="100%",
        id="overview"
    )


def web_applications_section() -> rx.Component:
    """Web applications projects section."""
    return rx.vstack(
        rx.heading(
            "Web Applications",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="web-applications"
        ),
        
        rx.grid(
            project_card(
                title="Portfolio Website",
                description="This very website! Built with Reflex framework, featuring a clean documentation-style layout inspired by OpenAuth, responsive design, and modern UI components.",
                technologies=["Reflex", "Python", "Responsive Design", "CSS"],
                github_url="https://github.com/unfortunatelyalex/portfolio",
                demo_url="/",
                icon="globe"
            ),
            
            project_card(
                title="Task Management App",
                description="A full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.",
                technologies=["React", "FastAPI", "PostgreSQL", "WebSocket"],
                github_url="https://github.com/unfortunatelyalex/task-manager",
                demo_url="https://tasks.alexportfolio.dev",
                icon="square-check"
            ),
            
            project_card(
                title="Weather Dashboard",
                description="Interactive weather dashboard with location-based forecasts, historical data visualization, and weather alerts.",
                technologies=["Vue.js", "Express.js", "Chart.js", "OpenWeather API"],
                github_url="https://github.com/unfortunatelyalex/weather-dash",
                demo_url="https://weather.alexportfolio.dev",
                icon="cloud"
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2", "1024px": "3"}),
            spacing="6",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def data_science_section() -> rx.Component:
    """Data science projects section."""
    return rx.vstack(
        rx.heading(
            "Data Science & Analytics",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="data-science"
        ),
        
        rx.grid(
            project_card(
                title="Sales Analytics Dashboard",
                description="Interactive dashboard for analyzing sales data with predictive modeling, trend analysis, and automated reporting.",
                technologies=["Python", "Pandas", "Plotly", "Streamlit", "Scikit-learn"],
                github_url="https://github.com/unfortunatelyalex/sales-analytics",
                demo_url="https://sales-analytics.streamlit.app",
                icon="bar-chart"
            ),
            
            project_card(
                title="Customer Segmentation",
                description="Machine learning project for customer segmentation using clustering algorithms and behavioral analysis.",
                technologies=["Python", "Scikit-learn", "Matplotlib", "Seaborn", "K-Means"],
                github_url="https://github.com/unfortunatelyalex/customer-segmentation",
                icon="users"
            ),
            
            project_card(
                title="Stock Price Predictor",
                description="Time series analysis and prediction model for stock prices using LSTM neural networks and financial indicators.",
                technologies=["Python", "TensorFlow", "yfinance", "Pandas", "LSTM"],
                github_url="https://github.com/unfortunatelyalex/stock-predictor",
                icon="trending-up"
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2", "1024px": "3"}),
            spacing="6",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def open_source_section() -> rx.Component:
    """Open source contributions section."""
    return rx.vstack(
        rx.heading(
            "Open Source Contributions",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="open-source"
        ),
        
        rx.grid(
            project_card(
                title="Reflex Components",
                description="Custom components and utilities for the Reflex framework, including advanced layout components and UI widgets.",
                technologies=["Python", "Reflex", "React", "TypeScript"],
                github_url="https://github.com/unfortunatelyalex/reflex-components",
                icon="package"
            ),
            
            project_card(
                title="Python Utils Library",
                description="Collection of utility functions and decorators for Python development, focusing on data processing and web scraping.",
                technologies=["Python", "Pytest", "Poetry", "GitHub Actions"],
                github_url="https://github.com/unfortunatelyalex/python-utils",
                icon="wrench"
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2"}),
            spacing="6",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def projects():
    """Projects page with all portfolio projects."""
    
    # Define sections for "On this page" navigation
    page_sections = [
        {"title": "Overview", "href": "#overview"},
        {"title": "Web Applications", "href": "#web-applications"},
        {"title": "Data Science", "href": "#data-science"},
        {"title": "Open Source", "href": "#open-source"}
    ]
    
    # Page content
    content = rx.vstack(
        projects_overview(),
        web_applications_section(),
        data_science_section(),
        open_source_section(),
        spacing="9",
        align_items="start",
        width="100%"
    )
    
    return page_layout(
        content=content,
        title="Projects",
        on_page_sections=page_sections,
        max_width="6xl"
    )
