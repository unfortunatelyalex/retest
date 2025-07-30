# site/components/on_page_navigation.py
import reflex as rx


def on_page_navigation(sections: list[dict]) -> rx.Component:
    """On this page navigation component for easy section jumping.
    
    Args:
        sections: List of dicts with 'title' and 'href' keys
        Example: [{"title": "Overview", "href": "#overview"}, {"title": "Skills", "href": "#skills"}]
    """
    if not sections:
        return rx.spacer()
    
    return rx.card(
        rx.vstack(
            rx.text(
                "On this page",
                size="3",
                weight="medium",
                color=rx.color("gray", 12),
                margin_bottom="3"
            ),
            rx.vstack(
                *[
                    rx.link(
                        rx.text(
                            section["title"],
                            size="2",
                            color=rx.color("gray", 11),
                            style={
                                "_hover": {
                                    "color": rx.color("accent", 11),
                                    "transition": "color 0.15s ease"
                                }
                            }
                        ),
                        href=section["href"],
                        style={
                            "text_decoration": "none",
                            "display": "block",
                            "padding": "0.25rem 0"
                        }
                    )
                    for section in sections
                ],
                spacing="1",
                align_items="start",
                width="100%"
            ),
            spacing="2",
            align_items="start",
            width="100%"
        ),
        size="2",
        style={
            "background_color": rx.color("gray", 2, alpha=True),
            "border": f"1px solid {rx.color('gray', 4)}",
            "margin_bottom": "2rem"
        }
    )
