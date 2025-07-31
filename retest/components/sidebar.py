"""Sidebar navigation component for the portfolio website."""
import reflex as rx
from ..state import NavigationState, PortfolioState
from ..styles import get_sidebar_styles, LAYOUT


def nav_item(icon: str, text: str, href: str, is_active, indent: int = 0) -> rx.Component:
    """Create a navigation item for the sidebar."""
    margin_left = f"{indent * 20}px" if indent > 0 else "0px"
    
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20),
            rx.cond(
                is_active,
                rx.text(
                    text,
                    weight="medium",
                    color=rx.color("iris", 11),
                ),
                rx.text(
                    text,
                    weight="regular", 
                    color=rx.color("gray", 11),
                ),
            ),
            align="center",
            gap="12px",
            padding="8px 12px",
            border_radius="6px",
            background=rx.cond(is_active, rx.color("iris", 3), "transparent"),
            _hover={
                "background": rx.cond(is_active, rx.color("iris", 3), rx.color("iris", 2))
            },
            width="100%",
            margin_left=margin_left,
        ),
        href=href,
        text_decoration="none",
        width="100%",
    )
def nav_section(title: str, items: list, is_expanded: bool = True) -> rx.Component:
    """Navigation section with collapsible items."""
    return rx.vstack(
        # Section header
        rx.hstack(
            rx.text(
                title,
                size="1",
                weight="bold",
                color=rx.color("gray", 10),
                text_transform="uppercase",
                letter_spacing="0.05em",
            ),
            rx.icon(
                "chevron-down" if is_expanded else "chevron-right",
                size=14,
                color=rx.color("gray", 10),
            ),
            justify="between",
            align="center",
            width="100%",
            padding="0.5rem 1rem",
            style={
                "cursor": "pointer",
                "_hover": {
                    "background_color": rx.color("gray", 2),
                },
                "border_radius": "4px",
            },
        ),
        
        # Section items
        rx.cond(
            is_expanded,
            rx.vstack(
                *items,
                spacing="0",
                width="100%",
            ),
            rx.fragment(),
        ),
        
        spacing="1",
        width="100%",
        align="start",
    )


def projects_nav() -> rx.Component:
    """Projects navigation subsection."""
    return rx.foreach(
        PortfolioState.projects,
        lambda project: nav_item(
            "folder",
            project["name"],
            f"/projects/{project['id']}",
            NavigationState.current_page == f"projects/{project['id']}",
            indent=1,
        ),
    )


def blog_nav() -> rx.Component:
    """Blog navigation subsection."""
    return rx.foreach(
        PortfolioState.blog_posts,
        lambda post: nav_item(
            "file-text",
            post["title"],
            f"/blog/{post['id']}",
            NavigationState.current_page == f"blog/{post['id']}",
            indent=1,
        ),
    )


def skills_nav() -> rx.Component:
    """Skills navigation subsection."""
    return rx.vstack(
        nav_item("code", "Languages", "/skills#languages", False, indent=1),
        nav_item("layers", "Frameworks", "/skills#frameworks", False, indent=1), 
        nav_item("wrench", "Tools", "/skills#tools", False, indent=1),
        spacing="0",
        width="100%",
    )


def sidebar() -> rx.Component:
    """Main sidebar navigation."""
    return rx.desktop_only(
        rx.box(
            rx.vstack(
                # Profile section at top
                rx.vstack(
                    rx.avatar(
                        fallback="A",
                        size="6",
                        radius="full",
                        style={
                            "border": f"3px solid {rx.color('blue', 6)}",
                        },
                    ),
                    rx.vstack(
                        rx.heading(PortfolioState.name, size="4", weight="bold"),
                        rx.text(
                            PortfolioState.title,
                            size="2",
                            color=rx.color("gray", 10),
                        ),
                        spacing="0",
                        align="center",
                    ),
                    spacing="3",
                    align="center",
                    width="100%",
                    padding="2rem 1rem 1.5rem",
                    border_bottom=f"1px solid {rx.color('gray', 4)}",
                ),
                
                # Navigation sections
                rx.vstack(
                    # Main navigation
                    nav_item("user", "About Me", "/", NavigationState.current_page == "about"),
                    
                    # Projects section
                    nav_section(
                        "Projects",
                        [
                            nav_item("briefcase", "All Projects", "/projects", NavigationState.current_page == "projects"),
                            projects_nav(),
                        ],
                    ),
                    
                    # Skills section
                    nav_section(
                        "Skills",
                        [
                            nav_item("brain", "Overview", "/skills", NavigationState.current_page == "skills"),
                            skills_nav(),
                        ],
                    ),
                    
                    # Blog section
                    nav_section(
                        "Blog",
                        [
                            nav_item("book-open", "All Posts", "/blog", NavigationState.current_page == "blog"),
                            blog_nav(),
                        ],
                    ),
                    
                    # Contact
                    nav_item("mail", "Contact", "/contact", NavigationState.current_page == "contact"),
                    
                    spacing="2",
                    width="100%",
                    padding="1rem",
                ),
                
                spacing="0",
                height="100%",
                overflow_y="auto",
            ),
            style={
                **get_sidebar_styles(),
                "width": LAYOUT["sidebar_width"],
            },
        )
    )


def mobile_sidebar() -> rx.Component:
    """Mobile sidebar overlay."""
    return rx.mobile_and_tablet(
        rx.cond(
            NavigationState.mobile_menu_open,
            rx.box(
                # Backdrop
                rx.box(
                    style={
                        "position": "fixed",
                        "top": "0",
                        "left": "0", 
                        "width": "100%",
                        "height": "100%",
                        "background_color": "rgba(0, 0, 0, 0.5)",
                        "z_index": "1998",
                    },
                    on_click=lambda: NavigationState.toggle_mobile_menu,
                ),
                
                # Sidebar content
                rx.box(
                    rx.vstack(
                        # Close button
                        rx.hstack(
                            rx.heading("Navigation", size="4"),
                            rx.button(
                                rx.icon("x", size=20),
                                on_click=lambda: NavigationState.toggle_mobile_menu,
                                variant="ghost",
                                size="2",
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                            padding="1rem",
                            border_bottom=f"1px solid {rx.color('gray', 4)}",
                        ),
                        
                        # Navigation items (simplified for mobile)
                        rx.vstack(
                            nav_item("user", "About", "/", NavigationState.current_page == "about"),
                            nav_item("briefcase", "Projects", "/projects", NavigationState.current_page == "projects"),
                            nav_item("brain", "Skills", "/skills", NavigationState.current_page == "skills"),
                            nav_item("book-open", "Blog", "/blog", NavigationState.current_page == "blog"),
                            nav_item("mail", "Contact", "/contact", NavigationState.current_page == "contact"),
                            spacing="1",
                            width="100%",
                            padding="1rem",
                        ),
                        
                        spacing="0",
                        width="100%",
                        height="100%",
                    ),
                    style={
                        "position": "fixed",
                        "top": "0",
                        "left": "0",
                        "width": "280px",
                        "height": "100%",
                        "background_color": rx.color("gray", 1),
                        "border_right": f"1px solid {rx.color('gray', 4)}",
                        "z_index": "1999",
                        "overflow_y": "auto",
                        "transform": "translateX(0)",
                        "transition": "transform 0.3s ease",
                    },
                ),
            ),
            rx.fragment(),
        )
    )
