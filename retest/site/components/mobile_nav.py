# site/components/mobile_nav.py
import reflex as rx

def mobile_navigation() -> rx.Component:
    """Mobile-friendly navigation component."""
    return rx.box(
        rx.mobile_and_tablet(
            rx.card(
                rx.hstack(
                    rx.link(
                        rx.vstack(
                            rx.icon("home", size=20),
                            rx.text("Home", size="1"),
                            align_items="center",
                            spacing="1"
                        ),
                        href="/",
                        style={"text_decoration": "none"}
                    ),
                    rx.link(
                        rx.vstack(
                            rx.icon("book-open", size=20),
                            rx.text("Blog", size="1"),
                            align_items="center",
                            spacing="1"
                        ),
                        href="/blog",
                        style={"text_decoration": "none"}
                    ),
                    rx.link(
                        rx.vstack(
                            rx.icon("user", size=20),
                            rx.text("About", size="1"),
                            align_items="center",
                            spacing="1"
                        ),
                        href="/#about",
                        style={"text_decoration": "none"}
                    ),
                    rx.link(
                        rx.vstack(
                            rx.icon("mail", size=20),
                            rx.text("Contact", size="1"),
                            align_items="center",
                            spacing="1"
                        ),
                        href="/#contact",
                        style={"text_decoration": "none"}
                    ),
                    justify="between",
                    align_items="center",
                    width="100%",
                    padding="0.75rem"
                ),
                style={
                    "position": "fixed",
                    "bottom": "1rem",
                    "left": "1rem",
                    "right": "1rem",
                    "z_index": "1000",
                    "backdrop_filter": "blur(10px)"
                }
            )
        ),
        rx.desktop_only(
            rx.spacer()  # No mobile nav on desktop
        )
    )
