"""Contact page for the portfolio website."""

import reflex as rx
from ..components.layout import page_layout, footer
from ..components.page_nav import page_section, tip_box
from ..state import PortfolioState


def contact_page() -> rx.Component:
    """Contact page content."""
    # Define page sections for navigation
    sections = [
        {"id": "get-in-touch", "title": "Get in Touch"},
        {"id": "contact-form", "title": "Contact Form"},
        {"id": "social-media", "title": "Social Media"},
        {"id": "response-time", "title": "Response Time"},
    ]

    return page_layout(
        title="Contact",
        description="Let's connect! Reach out for collaborations, opportunities, or just to say hello.",
        sections=sections,
        children=rx.vstack(
            # Get in touch section
            page_section(
                title="Get in Touch",
                id="get-in-touch",
                children=rx.vstack(
                    rx.text(
                        """
                        I'm always excited to connect with fellow developers, potential collaborators, 
                        and anyone interested in technology. Whether you have a project idea, job 
                        opportunity, or just want to chat about development, I'd love to hear from you!
                        """,
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Quick contact info
                    rx.grid(
                        # Email
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("mail", size=24, color=rx.color("blue", 9)),
                                    rx.heading(
                                        "Email", size="4", color=rx.color("blue", 9)
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.text(
                                    PortfolioState.email,
                                    size="3",
                                    weight="medium",
                                    color=rx.color("gray", 12),
                                ),
                                rx.text(
                                    "Best for project inquiries and professional matters",
                                    size="2",
                                    color=rx.color("gray", 10),
                                ),
                                rx.link(
                                    rx.button(
                                        "Send Email",
                                        size="2",
                                        color_scheme="blue",
                                    ),
                                    href=f"mailto:{PortfolioState.email}",
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                            ),
                            padding="2rem",
                            background_color=rx.color("blue", 2),
                            border_radius="12px",
                            border=f"1px solid {rx.color('blue', 4)}",
                            text_align="center",
                        ),
                        # Response time
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "clock", size=24, color=rx.color("green", 9)
                                    ),
                                    rx.heading(
                                        "Response Time",
                                        size="4",
                                        color=rx.color("green", 9),
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.text(
                                    "24-48 hours",
                                    size="3",
                                    weight="medium",
                                    color=rx.color("gray", 12),
                                ),
                                rx.text(
                                    "I typically respond within 1-2 business days",
                                    size="2",
                                    color=rx.color("gray", 10),
                                ),
                                spacing="3",
                                align="center",
                                width="100%",
                            ),
                            padding="2rem",
                            background_color=rx.color("green", 2),
                            border_radius="12px",
                            border=f"1px solid {rx.color('green', 4)}",
                            text_align="center",
                        ),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ),
                    tip_box(
                        "For urgent matters, please mention it in your email subject line.",
                        type="info",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Contact form section
            page_section(
                title="Contact Form",
                id="contact-form",
                children=rx.vstack(
                    rx.text(
                        "Fill out the form below and I'll get back to you as soon as possible:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Contact form
                    rx.form(
                        rx.vstack(
                            # Name and email row
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Name *", size="2", weight="medium"),
                                    rx.input(
                                        placeholder="Your full name",
                                        name="name",
                                        required=True,
                                        width="100%",
                                    ),
                                    align="start",
                                    spacing="1",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.text("Email *", size="2", weight="medium"),
                                    rx.input(
                                        placeholder="your.email@example.com",
                                        name="email",
                                        type="email",
                                        required=True,
                                        width="100%",
                                    ),
                                    align="start",
                                    spacing="1",
                                    width="100%",
                                ),
                                spacing="4",
                                width="100%",
                            ),
                            # Subject
                            rx.vstack(
                                rx.text("Subject *", size="2", weight="medium"),
                                rx.input(
                                    placeholder="What's this about?",
                                    name="subject",
                                    required=True,
                                    width="100%",
                                ),
                                align="start",
                                spacing="1",
                                width="100%",
                            ),
                            # Message
                            rx.vstack(
                                rx.text("Message *", size="2", weight="medium"),
                                rx.text_area(
                                    placeholder="Tell me about your project, question, or just say hello...",
                                    name="message",
                                    required=True,
                                    height="120px",
                                    width="100%",
                                ),
                                align="start",
                                spacing="1",
                                width="100%",
                            ),
                            # Submit button
                            rx.button(
                                rx.hstack(
                                    rx.icon("send", size=18),
                                    rx.text("Send Message"),
                                    spacing="2",
                                    align="center",
                                ),
                                size="3",
                                color_scheme="blue",
                                type="submit",
                                width="fit-content",
                            ),
                            spacing="4",
                            align="start",
                            width="100%",
                        ),
                        width="100%",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # Social media section
            page_section(
                title="Social Media & Professional Networks",
                id="social-media",
                children=rx.vstack(
                    rx.text(
                        "Connect with me on various platforms:",
                        size="3",
                        color=rx.color("gray", 11),
                        line_height="1.6",
                    ),
                    # Social links
                    rx.grid(
                        # GitHub
                        rx.link(
                            rx.box(
                                rx.vstack(
                                    rx.icon(
                                        "github", size=32, color=rx.color("gray", 12)
                                    ),
                                    rx.heading("GitHub", size="4"),
                                    rx.text(
                                        "Check out my code and repositories",
                                        size="2",
                                        color=rx.color("gray", 10),
                                        text_align="center",
                                    ),
                                    spacing="2",
                                    align="center",
                                    width="100%",
                                ),
                                padding="2rem",
                                background_color=rx.color("gray", 2),
                                border_radius="12px",
                                border=f"1px solid {rx.color('gray', 4)}",
                                _hover={
                                    "border_color": rx.color("gray", 6),
                                    "transform": "translateY(-2px)",
                                    "transition": "all 0.2s ease",
                                },
                                text_align="center",
                                width="100%",
                            ),
                            href=PortfolioState.github_url,
                            is_external=True,
                            style={"text_decoration": "none"},
                        ),
                        # LinkedIn
                        rx.link(
                            rx.box(
                                rx.vstack(
                                    rx.icon(
                                        "linkedin", size=32, color=rx.color("blue", 9)
                                    ),
                                    rx.heading("LinkedIn", size="4"),
                                    rx.text(
                                        "Professional network and career updates",
                                        size="2",
                                        color=rx.color("gray", 10),
                                        text_align="center",
                                    ),
                                    spacing="2",
                                    align="center",
                                    width="100%",
                                ),
                                padding="2rem",
                                background_color=rx.color("blue", 2),
                                border_radius="12px",
                                border=f"1px solid {rx.color('blue', 4)}",
                                _hover={
                                    "border_color": rx.color("blue", 6),
                                    "transform": "translateY(-2px)",
                                    "transition": "all 0.2s ease",
                                },
                                text_align="center",
                                width="100%",
                            ),
                            href=PortfolioState.linkedin_url,
                            is_external=True,
                            style={"text_decoration": "none"},
                        ),
                        # Twitter/X (optional)
                        rx.link(
                            rx.box(
                                rx.vstack(
                                    rx.icon(
                                        "twitter", size=32, color=rx.color("cyan", 9)
                                    ),
                                    rx.heading("Twitter", size="4"),
                                    rx.text(
                                        "Thoughts, updates, and tech discussions",
                                        size="2",
                                        color=rx.color("gray", 10),
                                        text_align="center",
                                    ),
                                    spacing="2",
                                    align="center",
                                    width="100%",
                                ),
                                padding="2rem",
                                background_color=rx.color("cyan", 2),
                                border_radius="12px",
                                border=f"1px solid {rx.color('cyan', 4)}",
                                _hover={
                                    "border_color": rx.color("cyan", 6),
                                    "transform": "translateY(-2px)",
                                    "transition": "all 0.2s ease",
                                },
                                text_align="center",
                                width="100%",
                            ),
                            href="https://twitter.com/username",
                            is_external=True,
                            style={"text_decoration": "none"},
                        ),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
            ),
            # FAQ/Additional info
            rx.box(
                rx.vstack(
                    rx.heading("Frequently Asked", size="5", weight="medium"),
                    rx.vstack(
                        rx.vstack(
                            rx.text(
                                "What type of projects are you interested in?",
                                size="3",
                                weight="medium",
                                color=rx.color("gray", 12),
                            ),
                            rx.text(
                                "I'm interested in web applications, APIs, developer tools, and open-source contributions. I particularly enjoy projects involving Python, React, or interesting technical challenges.",
                                size="2",
                                color=rx.color("gray", 10),
                                line_height="1.5",
                            ),
                            align="start",
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text(
                                "Are you available for freelance work?",
                                size="3",
                                weight="medium",
                                color=rx.color("gray", 12),
                            ),
                            rx.text(
                                "It depends on my current commitments, but I'm always open to discussing interesting opportunities. Feel free to reach out with your project details.",
                                size="2",
                                color=rx.color("gray", 10),
                                line_height="1.5",
                            ),
                            align="start",
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text(
                                "Do you mentor or provide code reviews?",
                                size="3",
                                weight="medium",
                                color=rx.color("gray", 12),
                            ),
                            rx.text(
                                "Yes! I enjoy helping other developers grow. If you're looking for mentorship or code review, please mention it in your message.",
                                size="2",
                                color=rx.color("gray", 10),
                                line_height="1.5",
                            ),
                            align="start",
                            spacing="1",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    spacing="4",
                    align="start",
                    width="100%",
                ),
                padding="2rem",
                background_color=rx.color("gray", 2),
                border_radius="12px",
                border=f"1px solid {rx.color('gray', 4)}",
                margin_top="2rem",
            ),
            # Footer
            footer(),
            spacing="6",
            align="start",
            width="100%",
        ),
    )
