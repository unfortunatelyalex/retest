# site/components/sidebar_navigation.py
import reflex as rx
from retest.site.state import SidebarState


def navigation_link(
    text: str, 
    href: str, 
    icon: str, 
    is_active: bool = False,
    has_children: bool = False,
    children: list | None = None
) -> rx.Component:
    """Create a navigation link with optional icon and active state."""
    return rx.vstack(
        rx.link(
            rx.hstack(
                rx.icon(tag=icon, size=16),
                rx.text(
                    text,
                    size="2",
                    weight="medium" if is_active else "regular",
                    color=rx.cond(
                        is_active,
                        rx.color("accent", 11),
                        rx.color("gray", 11)
                    )
                ),
                rx.spacer(),
                rx.cond(
                    has_children,
                    rx.icon(
                        tag="chevron-right",
                        size=14,
                        color=rx.color("gray", 9)
                    ),
                    rx.spacer()
                ),
                align_items="center",
                justify="between",
                width="100%",
                padding_x="3",
                padding_y="2",
                border_radius="md",
                style={
                    "_hover": {
                        "background_color": rx.color("gray", 2),
                        "transition": "background-color 0.15s ease",
                    }
                }
            ),
            href=href,
            style={
                "text_decoration": "none",
                "display": "block",
                "width": "100%",
                "border_radius": "md",
                "background_color": rx.cond(
                    is_active,
                    rx.color("accent", 2),
                    "transparent"
                ),
            }
        ),
        # Children submenu (if any)
        rx.cond(
            has_children & (children is not None),
            rx.vstack(
                *[
                    rx.link(
                        rx.hstack(
                            rx.box(width="20px"),  # Indent
                            rx.text(
                                child["text"], 
                                size="1", 
                                color=rx.color("gray", 10)
                            ),
                            align_items="center",
                            padding_x="3",
                            padding_y="1",
                            border_radius="md",
                            style={
                                "_hover": {
                                    "background_color": rx.color("gray", 2)
                                }
                            }
                        ),
                        href=child["href"],
                        style={"text_decoration": "none", "display": "block"}
                    )
                    for child in (children or [])
                ],
                spacing="1",
                align_items="stretch",
                width="100%",
                margin_left="2"
            ),
            rx.spacer()
        ),
        spacing="1",
        align_items="stretch",
        width="100%"
    )


def navigation_section(title: str, links: list) -> rx.Component:
    """Create a navigation section with a title and links."""
    return rx.vstack(
        rx.text(
            title,
            size="1",
            weight="bold",
            text_transform="uppercase",
            letter_spacing="0.05em",
            color=rx.color("gray", 9),
            margin_bottom="2"
        ),
        rx.vstack(
            *[
                navigation_link(
                    text=link["text"],
                    href=link["href"], 
                    icon=link["icon"],
                    is_active=link.get("is_active", False),
                    has_children=link.get("has_children", False),
                    children=link.get("children", None)
                )
                for link in links
            ],
            spacing="1",
            align_items="stretch",
            width="100%"
        ),
        spacing="2",
        align_items="start",
        width="100%"
    )


def sidebar_navigation() -> rx.Component:
    """Main sidebar navigation component following OpenAuth design patterns."""
    
    # Define navigation structure
    intro_links = [
        {
            "text": "Introduction", 
            "href": "/", 
            "icon": "home",
            "is_active": True
        },
        {
            "text": "About Me",
            "href": "/about", 
            "icon": "user"
        }
    ]
    
    portfolio_links = [
        {
            "text": "Projects",
            "href": "/projects",
            "icon": "folder",
            "has_children": True,
            "children": [
                {"text": "Web Applications", "href": "/projects/web"},
                {"text": "Data Science", "href": "/projects/data"},
                {"text": "Open Source", "href": "/projects/open-source"}
            ]
        },
        {
            "text": "Skills & Experience", 
            "href": "/skills",
            "icon": "code"
        },
        {
            "text": "Blog",
            "href": "/blog",
            "icon": "book-open"
        }
    ]
    
    contact_links = [
        {
            "text": "Contact", 
            "href": "/contact",
            "icon": "mail"
        }
    ]
    
    return rx.box(
        # Sidebar container
        rx.vstack(
            # Logo/Brand area
            rx.hstack(
                rx.text(
                    "Portfolio",
                    size="4",
                    weight="bold",
                    color=rx.color("accent", 11)
                ),
                rx.spacer(),
                # Mobile close button
                rx.mobile_and_tablet(
                    rx.icon_button(
                        rx.icon(tag="x", size=16),
                        variant="ghost",
                        size="2",
                        on_click=SidebarState.close_sidebar,
                        style={"cursor": "pointer"}
                    )
                ),
                align_items="center",
                justify="between",
                width="100%",
                padding_bottom="4",
                border_bottom=f"1px solid {rx.color('gray', 4)}"
            ),
            
            # Navigation sections
            rx.vstack(
                navigation_section("Introduction", intro_links),
                navigation_section("Portfolio", portfolio_links), 
                navigation_section("Connect", contact_links),
                spacing="6",
                align_items="start",
                width="100%",
                padding_y="4"
            ),
            
            rx.spacer(),
            
            # Footer with version/update info
            rx.vstack(
                rx.divider(),
                rx.text(
                    "Last updated — July 30, 2025",
                    size="1",
                    color=rx.color("gray", 9)
                ),
                spacing="2",
                align_items="start",
                width="100%"
            ),
            
            spacing="4",
            align_items="start",
            height="100vh",
            width="100%",
            padding="6",
            overflow_y="auto"
        ),
        
        # Sidebar styling
        background_color=rx.color("gray", 1),
        border_right=f"1px solid {rx.color('gray', 4)}",
        position="fixed",
        left="0",
        top="0",
        height="100vh",
        width="280px",
        z_index="1000",
        
        # Responsive behavior
        style={
            # Desktop: always visible
            "@media (min-width: 768px)": {
                "display": "block"
            },
            # Mobile: conditional visibility based on state
            "@media (max-width: 767px)": {
                "display": rx.cond(SidebarState.is_open, "block", "none"),
                "box_shadow": "0 4px 24px rgba(0,0,0,0.15)",
                "backdrop_filter": "blur(10px)"
            }
        }
    )


def mobile_sidebar_overlay() -> rx.Component:
    """Dark overlay for mobile sidebar."""
    return rx.mobile_and_tablet(
        rx.cond(
            SidebarState.is_open,
            rx.box(
                position="fixed",
                top="0",
                left="0", 
                right="0",
                bottom="0",
                background_color="rgba(0,0,0,0.5)",
                z_index="999",
                on_click=SidebarState.close_sidebar,
                style={"cursor": "pointer"}
            ),
            rx.spacer()
        )
    )


def mobile_sidebar_toggle() -> rx.Component:
    """Mobile hamburger menu button."""
    return rx.mobile_and_tablet(
        rx.icon_button(
            rx.icon(tag="menu", size=18),
            variant="ghost",
            size="3",
            on_click=SidebarState.open_sidebar,
            style={
                "cursor": "pointer",
                "position": "fixed",
                "top": "1rem",
                "left": "1rem", 
                "z_index": "1001",
                "background_color": rx.color("gray", 2),
                "border": f"1px solid {rx.color('gray', 4)}",
                "backdrop_filter": "blur(10px)"
            }
        )
    )
