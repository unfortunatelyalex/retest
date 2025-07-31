"""On this page navigation component."""
import reflex as rx
from ..state import NavigationState


def on_this_page() -> rx.Component:
    """On this page navigation for internal anchors."""
    return rx.cond(
        NavigationState.current_sections,
        rx.box(
            rx.vstack(
                rx.heading(
                    "On this page",
                    size="3",
                    weight="medium",
                    color=rx.color("gray", 12),
                ),
                rx.vstack(
                    rx.foreach(
                        NavigationState.current_sections,
                        lambda section: rx.link(
                            rx.text(
                                section["title"],
                                size="2",
                                color=rx.color("gray", 11),
                                _hover={
                                    "color": rx.color("blue", 9),
                                },
                            ),
                            href=f"#{section['id']}",
                            style={
                                "text_decoration": "none",
                                "display": "block",
                                "padding": "0.25rem 0",
                                "border_left": f"2px solid {rx.color('gray', 4)}",
                                "padding_left": "0.75rem",
                                "margin_left": "0.5rem",
                                "_hover": {
                                    "border_left_color": rx.color("blue", 6),
                                },
                                "transition": "border-color 0.2s ease",
                            },
                        ),
                    ),
                    spacing="0",
                    align="start",
                    width="100%",
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            style={
                "background_color": rx.color("gray", 2),
                "border": f"1px solid {rx.color('gray', 4)}",
                "border_radius": "8px",
                "padding": "1.5rem",
                "margin_bottom": "2rem",
            },
        ),
        rx.fragment(),
    )


def page_section(
    title: str,
    id: str,
    children: rx.Component,
    level: int = 2,
) -> rx.Component:
    """Page section with anchor link."""
    heading_component = rx.heading(
        rx.hstack(
            title,
            rx.link(
                rx.icon("hash", size=16, color=rx.color("gray", 8)),
                href=f"#{id}",
                style={
                    "text_decoration": "none",
                    "opacity": "0",
                    "_hover": {"opacity": "1"},
                    "transition": "opacity 0.2s ease",
                },
            ),
            spacing="2",
            align="center",
            _hover={
                "& a": {"opacity": "1"},
            },
        ),
        id=id,
        size="6" if level == 2 else "5" if level == 3 else "4",
        weight="medium",
        color=rx.color("gray", 12),
        margin_top="2rem" if level == 2 else "1.5rem",
        margin_bottom="1rem",
    )
    
    return rx.vstack(
        heading_component,
        children,
        spacing="3",
        align="start",
        width="100%",
    )


def tip_box(content: str, type: str = "info") -> rx.Component:
    """Tip/note box component."""
    icon_map = {
        "info": "info",
        "tip": "lightbulb",
        "warning": "alert-triangle",
        "error": "alert-circle",
    }
    
    icon = icon_map.get(type, "info")
    
    return rx.box(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(
                content,
                size="2",
                color=rx.color("gray", 11),
                font_style="italic",
                line_height="1.6",
            ),
            spacing="3",
            align="start",
        ),
        style={
            "background_color": rx.color("gray", 2),
            "border_left": f"4px solid {rx.color('blue', 6)}",
            "border_radius": "0 8px 8px 0",
            "padding": "1rem",
            "margin": "1rem 0",
        },
    )
