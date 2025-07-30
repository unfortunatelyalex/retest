# site/components/page_layout.py
import reflex as rx
from retest.site.components.sidebar_navigation import (
    sidebar_navigation, 
    mobile_sidebar_overlay, 
    mobile_sidebar_toggle
)
from retest.site.components.header import site_header
from retest.site.components.on_page_navigation import on_page_navigation


def page_layout(
    content: rx.Component,
    title: str = "",
    on_page_sections: list[dict] | None = None,
    max_width: str = "4xl"
) -> rx.Component:
    """Main page layout wrapper with sidebar, header, and content area.
    
    Args:
        content: The main page content
        title: Page title (displayed as h1)
        on_page_sections: Optional list of sections for "On this page" navigation
        max_width: Maximum width of content area
    """
    return rx.box(
        # Mobile sidebar overlay
        mobile_sidebar_overlay(),
        
        # Mobile hamburger menu
        mobile_sidebar_toggle(),
        
        # Sidebar navigation
        sidebar_navigation(),
        
        # Main content area
        rx.box(
            # Header
            site_header(),
            
            # Content area
            rx.container(
                rx.vstack(
                    # Page title
                    rx.cond(
                        title != "",
                        rx.heading(
                            title,
                            size="8",
                            weight="bold",
                            color=rx.color("gray", 12),
                            margin_bottom="4",
                            line_height="1.2"
                        ),
                        rx.spacer()
                    ),
                    
                    # On this page navigation
                    rx.cond(
                        (on_page_sections is not None) & (len(on_page_sections or []) > 0),
                        on_page_navigation(on_page_sections or []),
                        rx.spacer()
                    ),
                    
                    # Main content
                    content,
                    
                    spacing="6",
                    align_items="start",
                    width="100%",
                    min_height="calc(100vh - 100px)"
                ),
                max_width=max_width,
                padding_x="6",
                padding_y="8"
            ),
            
            # Main content area styling
            style={
                # Desktop: account for sidebar
                "@media (min-width: 768px)": {
                    "margin_left": "280px"
                },
                # Mobile: full width
                "@media (max-width: 767px)": {
                    "margin_left": "0"
                }
            }
        ),
        
        # Root container styling
        min_height="100vh",
        background_color=rx.color("gray", 1, alpha=True),
        style={
            # Typography improvements
            "font_family": "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
            "line_height": "1.6",
            "color": rx.color("gray", 12)
        }
    )
