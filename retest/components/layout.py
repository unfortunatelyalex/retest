"""Main layout component for the portfolio website."""

import reflex as rx
from .header import header, mobile_header
from .sidebar import sidebar, mobile_sidebar
from ..state import NavigationState
from ..styles import get_content_styles, LAYOUT


def layout(children: rx.Component) -> rx.Component:
    """Main layout with sidebar, header, and content area."""
    return rx.box(
        # Desktop layout
        rx.desktop_only(
            rx.box(
                # Sidebar
                sidebar(),
                # Header
                header(),
                # Main content area
                rx.box(
                    children,
                    style={
                        **get_content_styles(),
                        "margin_left": rx.cond(
                            NavigationState.sidebar_collapsed,
                            "60px",
                            LAYOUT["sidebar_width"],
                        ),
                    },
                ),
                style={
                    "position": "relative",
                    "min_height": "100vh",
                },
            )
        ),
        # Mobile layout
        rx.mobile_and_tablet(
            rx.box(
                # Mobile header
                mobile_header(),
                # Mobile sidebar overlay
                mobile_sidebar(),
                # Main content area
                rx.box(
                    children,
                    style={
                        "margin_top": LAYOUT["header_height"],
                        "padding": "1rem",
                        "min_height": f"calc(100vh - {LAYOUT['header_height']})",
                    },
                ),
                style={
                    "position": "relative",
                    "min_height": "100vh",
                },
            )
        ),
        style={
            "min_height": "100vh",
            "background_color": rx.color("gray", 1),
            "color": rx.color("gray", 12),
        },
    )


def page_layout(
    title: str,
    children: rx.Component,
    sections: list | None = None,
    description: str = "",
) -> rx.Component:
    """Page layout with title and optional sections."""
    from .page_nav import on_this_page

    # Note: pages can set sections via state on mount if needed.

    return layout(
        rx.vstack(
            # Page title
            rx.heading(
                title,
                size="8",
                weight="bold",
                color=rx.color("gray", 12),
                margin_bottom="1rem",
            ),
            # Page description
            rx.cond(
                description,
                rx.text(
                    description,
                    size="4",
                    color=rx.color("gray", 10),
                    margin_bottom="2rem",
                    line_height="1.6",
                ),
                rx.fragment(),
            ),
            # On this page navigation (desktop only)
            rx.desktop_only(on_this_page()),
            # Page content
            children,
            spacing="4",
            align="start",
            width="100%",
            max_width="900px",
        )
    )


def footer() -> rx.Component:
    """Footer component."""
    return rx.box(
        rx.vstack(
            rx.separator(width="100%", color_scheme="gray"),
            rx.hstack(
                rx.text(
                    "© 2025 Alex. Built with Reflex.",
                    size="2",
                    color=rx.color("gray", 10),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link(
                        "GitHub",
                        href="https://github.com/unfortunatelyalex",
                        size="2",
                        color=rx.color("gray", 10),
                        is_external=True,
                    ),
                    rx.text("•", color=rx.color("gray", 8)),
                    rx.link(
                        "LinkedIn",
                        href="https://linkedin.com/in/alexander-bonin-2758b5178/",
                        size="2",
                        color=rx.color("gray", 10),
                        is_external=True,
                    ),
                    rx.text("•", color=rx.color("gray", 8)),
                    rx.link(
                        "Contact",
                        href="/contact",
                        size="2",
                        color=rx.color("gray", 10),
                    ),
                    spacing="2",
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            spacing="3",
            padding="2rem 0",
            width="100%",
        ),
        margin_top="4rem",
    )
