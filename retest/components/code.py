"""Code block component with syntax highlighting."""

import reflex as rx


def code_block(
    code: str,
    language: str = "python",
    show_line_numbers: bool = False,
    filename: str = "",
    github_url: str = "",
) -> rx.Component:
    """Code block component with custom styling and header."""
    # For now, use a styled text block with monospace font
    # TODO: Add proper syntax highlighting when Reflex API is more flexible
    code_content = rx.box(
        rx.markdown(
            code,
            style={
                "font_family": "monospace",
                "font_size": "0.9rem",
                "line_height": "1.5",
                "padding": "0.5rem",
                "margin": "0",
                "background_color": "transparent",
                "border": "none",
                "overflow_x": "auto",
                "white_space": "pre",
                "color": rx.color("gray", 12),
            },
        ),
        style={
            "background_color": rx.color("gray", 2),
            "border": f"1px solid {rx.color('gray', 4)}",
            "border_radius": "0 0 8px 8px" if filename or github_url else "8px",
            "border_top": (
                "none" if filename or github_url else f"1px solid {rx.color('gray', 4)}"
            ),
            "width": "fit-content",
            "min_width": "100%",
        },
    )

    # Create the header that matches the code content width
    header = rx.cond(
        filename or github_url,
        rx.box(
            rx.hstack(
                rx.cond(
                    filename,
                    rx.text(
                        filename,
                        size="2",
                        weight="medium",
                        color=rx.color("gray", 11),
                        font_family="monospace",
                    ),
                    rx.fragment(),
                ),
                rx.spacer(),
                rx.cond(
                    github_url,
                    rx.link(
                        rx.hstack(
                            rx.icon("external-link", size=14),
                            rx.text("View source", size="1"),
                            spacing="1",
                            align="center",
                        ),
                        href=github_url,
                        is_external=True,
                        style={
                            "text_decoration": "none",
                            "color": rx.color("blue", 9),
                            "_hover": {
                                "color": rx.color("blue", 10),
                            },
                        },
                    ),
                    rx.fragment(),
                ),
                justify="between",
                align="center",
                width="100%",
                padding="0.5rem 1rem",
            ),
            style={
                "background_color": rx.color("gray", 3),
                "border_radius": "8px 8px 0 0",
                "border_bottom": f"1px solid {rx.color('gray', 4)}",
                "width": "fit-content",
                "min_width": "100%",
            },
        ),
        rx.fragment(),
    )

    return rx.vstack(
        header,
        code_content,
        spacing="0",
        align="start",
        style={
            "width": "fit-content",
            "min_width": "100%",
        },
    )


def inline_code(code: str) -> rx.Component:
    """Inline code component."""
    return rx.code(
        code,
        style={
            "background_color": rx.color("gray", 3),
            "color": rx.color("gray", 12),
            "padding": "0.1rem 0.3rem",
            "border_radius": "4px",
            "font_family": "monospace",
            "font_size": "0.9em",
        },
    )


def code_snippet(
    title: str,
    code: str,
    language: str = "python",
    description: str = "",
) -> rx.Component:
    """Code snippet with title and description."""
    return rx.vstack(
        rx.heading(title, size="4", weight="medium"),
        rx.cond(
            description,
            rx.text(
                description,
                size="2",
                color=rx.color("gray", 10),
                margin_bottom="1rem",
            ),
            rx.fragment(),
        ),
        code_block(code, language),
        spacing="3",
        align="start",
        width="100%",
    )
