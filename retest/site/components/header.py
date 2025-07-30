# site/components/header.py
import reflex as rx


def theme_toggle_button() -> rx.Component:
    """Theme toggle button with system/light/dark modes."""
    return rx.icon_button(
        rx.cond(
            rx.color_mode == "light",
            rx.icon(tag="sun", size=16),
            rx.icon(tag="moon", size=16),
        ),
        on_click=rx.toggle_color_mode,
        variant="ghost",
        size="2",
        radius="full",
        style={
            "_hover": {
                "background_color": rx.color("gray", 3),
                "transform": "scale(1.05)",
                "transition": "all 0.15s ease-in-out",
            }
        }
    )


def global_navigation_links() -> rx.Component:
    """Global navigation links (GitHub, Discord)."""
    return rx.hstack(
        rx.link(
            rx.icon_button(
                rx.icon(tag="github", size=16),
                variant="ghost",
                size="2",
                radius="full",
                style={
                    "_hover": {
                        "background_color": rx.color("gray", 3),
                        "transition": "background-color 0.15s ease",
                    }
                }
            ),
            href="https://github.com/unfortunatelyalex",
            is_external=True,
            style={"text_decoration": "none"}
        ),
        rx.link(
            rx.icon_button(
                rx.icon(tag="message-circle", size=16), 
                variant="ghost",
                size="2",
                radius="full",
                style={
                    "_hover": {
                        "background_color": rx.color("gray", 3),
                        "transition": "background-color 0.15s ease",
                    }
                }
            ),
            href="https://discord.gg/your-discord",
            is_external=True,
            style={"text_decoration": "none"}
        ),
        spacing="2",
        align_items="center"
    )


def site_header() -> rx.Component:
    """Main site header with theme toggle and global navigation."""
    return rx.box(
        rx.hstack(
            # Left side - empty on desktop (sidebar handles branding)
            rx.desktop_only(rx.spacer()),
            
            # Mobile - show page title 
            rx.mobile_and_tablet(
                rx.text(
                    "Portfolio",
                    size="4",
                    weight="bold",
                    color=rx.color("accent", 11)
                )
            ),
            
            rx.spacer(),
            
            # Right side - global navigation and theme toggle
            rx.hstack(
                global_navigation_links(),
                theme_toggle_button(),
                spacing="3",
                align_items="center"
            ),
            
            align_items="center",
            justify="between",
            width="100%",
            padding_x="6",
            padding_y="4",
        ),
        
        # Header styling
        background_color=rx.color("gray", 1, alpha=True),
        border_bottom=f"1px solid {rx.color('gray', 4)}",
        backdrop_filter="blur(10px)",
        position="sticky",
        top="0",
        z_index="100",
        
        # Responsive positioning
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
    )
