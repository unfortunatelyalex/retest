"""Header component for the portfolio website."""
import reflex as rx
from ..state import NavigationState
from ..styles import get_header_styles, get_link_styles, get_button_styles


def theme_toggle() -> rx.Component:
    """Theme toggle component with Light/Dark/Auto options."""
    return rx.button(
        rx.cond(
            rx.color_mode == "light",
            rx.icon("sun", size=18),
            rx.icon("moon", size=18),
        ),
        variant="ghost",
        size="2",
        on_click=rx.toggle_color_mode,
        style=get_button_styles("ghost"),
    )


def header() -> rx.Component:
    """Top header bar with global links and theme toggle."""
    return rx.desktop_only(
        rx.box(
            rx.hstack(
                # Logo/Brand - left side
                rx.hstack(
                    rx.heading("Portfolio", size="4", weight="medium"),
                    spacing="2",
                ),
                
                # Global links - right side
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.icon("github", size=18),
                            rx.text("GitHub", size="2"),
                            spacing="1",
                            align="center",
                        ),
                        href="https://github.com/username",
                        style=get_link_styles(),
                        is_external=True,
                    ),
                    rx.link(
                        rx.hstack(
                            rx.icon("linkedin", size=18), 
                            rx.text("LinkedIn", size="2"),
                            spacing="1",
                            align="center",
                        ),
                        href="https://linkedin.com/in/username",
                        style=get_link_styles(),
                        is_external=True,
                    ),
                    rx.link(
                        rx.hstack(
                            rx.icon("mail", size=18),
                            rx.text("Contact", size="2"),
                            spacing="1",
                            align="center",
                        ),
                        href="#contact",
                        style=get_link_styles(),
                    ),
                    theme_toggle(),
                    spacing="4",
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            style={
                **get_header_styles(),
                "left": "280px",  # Account for sidebar width
                "width": "calc(100% - 280px)",
            },
        )
    )


def mobile_header() -> rx.Component:
    """Mobile header with hamburger menu."""
    return rx.mobile_and_tablet(
        rx.box(
            rx.hstack(
                # Hamburger menu button
                rx.button(
                    rx.icon("menu", size=20),
                    on_click=lambda: NavigationState.toggle_mobile_menu,
                    variant="ghost",
                    size="2",
                    style=get_button_styles("ghost"),
                ),
                
                # Logo/Brand
                rx.heading("Portfolio", size="4", weight="medium"),
                
                # Theme toggle
                theme_toggle(),
                
                justify="between",
                align="center",
                width="100%",
            ),
            style={
                **get_header_styles(),
                "left": "0",
                "width": "100%",
            },
        )
    )
