import reflex as rx
from retest.site.components.page_layout import page_layout
from retest.site.state import ContactState


def contact_intro() -> rx.Component:
    """Contact page introduction."""
    return rx.vstack(
        rx.text(
            "I'm always interested in new opportunities, collaborations, and interesting conversations about technology. Whether you have a project in mind, want to discuss a potential role, or just want to chat about the latest in tech, I'd love to hear from you!",
            size="4",
            color=rx.color("gray", 11),
            line_height="1.7",
            margin_bottom="6"
        ),
        align_items="start",
        width="100%",
        id="overview"
    )


def contact_methods() -> rx.Component:
    """Contact methods section."""
    return rx.vstack(
        rx.heading(
            "Get in Touch",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="contact-methods"
        ),
        
        rx.grid(
            # Email
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="mail", size=24, color=rx.color("blue", 11)),
                        rx.heading("Email", size="4"),
                        align_items="center",
                        spacing="3"
                    ),
                    rx.text(
                        "For professional inquiries, project discussions, or general questions.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6",
                        margin_bottom="3"
                    ),
                    rx.link(
                        rx.button(
                            "alex@example.com",
                            variant="outline",
                            size="3"
                        ),
                        href="mailto:alex@example.com"
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("blue", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            # LinkedIn
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="linkedin", size=24, color=rx.color("blue", 11)),
                        rx.heading("LinkedIn", size="4"),
                        align_items="center",
                        spacing="3"
                    ),
                    rx.text(
                        "Connect with me professionally and see my career journey.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6",
                        margin_bottom="3"
                    ),
                    rx.link(
                        rx.button(
                            "Connect on LinkedIn",
                            variant="outline",
                            size="3"
                        ),
                        href="https://linkedin.com/in/alex-rodriguez-dev",
                        is_external=True
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("blue", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            # GitHub
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="github", size=24, color=rx.color("gray", 11)),
                        rx.heading("GitHub", size="4"),
                        align_items="center",
                        spacing="3"
                    ),
                    rx.text(
                        "Check out my code, contribute to projects, or start a discussion.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6",
                        margin_bottom="3"
                    ),
                    rx.link(
                        rx.button(
                            "View on GitHub",
                            variant="outline",
                            size="3"
                        ),
                        href="https://github.com/unfortunatelyalex",
                        is_external=True
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("gray", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            # Discord
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(tag="message-circle", size=24, color=rx.color("purple", 11)),
                        rx.heading("Discord", size="4"),
                        align_items="center",
                        spacing="3"
                    ),
                    rx.text(
                        "For casual conversations about tech, programming, or collaboration.",
                        size="2",
                        color=rx.color("gray", 10),
                        line_height="1.6",
                        margin_bottom="3"
                    ),
                    rx.link(
                        rx.button(
                            "Message on Discord",
                            variant="outline",
                            size="3"
                        ),
                        href="https://discord.gg/your-discord",
                        is_external=True
                    ),
                    align_items="start",
                    spacing="3"
                ),
                size="3",
                style={
                    "background_color": rx.color("gray", 2, alpha=True),
                    "border": f"1px solid {rx.color('gray', 4)}",
                    "_hover": {
                        "border_color": rx.color("purple", 6),
                        "transition": "border-color 0.2s ease"
                    }
                }
            ),
            
            columns=rx.breakpoints({"0px": "1", "768px": "2"}),
            spacing="4",
            width="100%"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def contact_form() -> rx.Component:
    """Contact form section."""
    return rx.vstack(
        rx.heading(
            "Send a Message",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="contact-form"
        ),
        
        rx.text(
            "Prefer to send a message directly? Use the form below and I'll get back to you as soon as possible.",
            size="3",
            color=rx.color("gray", 10),
            line_height="1.7",
            margin_bottom="6"
        ),
        
        rx.card(
            rx.form(
                rx.vstack(
                    # Name field
                    rx.vstack(
                        rx.text("Name", size="2", weight="medium"),
                        rx.input(
                            placeholder="Your name",
                            name="name",
                            value=ContactState.name,
                            on_change=ContactState.set_name,
                            size="3",
                            width="100%"
                        ),
                        rx.cond(
                            ContactState.name_error != "",
                            rx.text(
                                ContactState.name_error,
                                size="1",
                                color=rx.color("red", 11)
                            ),
                            rx.spacer()
                        ),
                        align_items="start",
                        spacing="1",
                        width="100%"
                    ),
                    
                    # Email field
                    rx.vstack(
                        rx.text("Email", size="2", weight="medium"),
                        rx.input(
                            placeholder="your.email@example.com",
                            name="email",
                            type="email",
                            value=ContactState.email,
                            on_change=ContactState.set_email,
                            size="3",
                            width="100%"
                        ),
                        rx.cond(
                            ContactState.email_error != "",
                            rx.text(
                                ContactState.email_error,
                                size="1",
                                color=rx.color("red", 11)
                            ),
                            rx.spacer()
                        ),
                        align_items="start",
                        spacing="1",
                        width="100%"
                    ),
                    
                    # Message field
                    rx.vstack(
                        rx.text("Message", size="2", weight="medium"),
                        rx.text_area(
                            placeholder="Tell me about your project, question, or just say hello!",
                            name="message",
                            value=ContactState.message,
                            on_change=ContactState.set_message,
                            rows="6",
                            size="3",
                            width="100%"
                        ),
                        rx.cond(
                            ContactState.message_error != "",
                            rx.text(
                                ContactState.message_error,
                                size="1",
                                color=rx.color("red", 11)
                            ),
                            rx.spacer()
                        ),
                        align_items="start",
                        spacing="1",
                        width="100%"
                    ),
                    
                    # Submit button
                    rx.button(
                        rx.cond(
                            ContactState.is_submitting,
                            rx.hstack(
                                rx.spinner(size="1"),
                                "Sending...",
                                spacing="2"
                            ),
                            rx.hstack(
                                rx.icon(tag="send", size=16),
                                "Send Message",
                                spacing="2"
                            )
                        ),
                        type="submit",
                        size="3",
                        disabled=ContactState.is_submitting,
                        style={
                            "cursor": rx.cond(ContactState.is_submitting, "not-allowed", "pointer")
                        }
                    ),
                    
                    # Success message
                    rx.cond(
                        ContactState.submit_success,
                        rx.callout(
                            "Thank you for your message! I'll get back to you soon.",
                            icon="check",
                            color_scheme="green",
                            size="2"
                        ),
                        rx.spacer()
                    ),
                    
                    spacing="6",
                    align_items="start",
                    width="100%"
                ),
                on_submit=ContactState.send_message,
                width="100%"
            ),
            size="4",
            style={
                "background_color": rx.color("gray", 2, alpha=True),
                "border": f"1px solid {rx.color('gray', 4)}"
            }
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def response_time() -> rx.Component:
    """Response time information."""
    return rx.vstack(
        rx.heading(
            "Response Time",
            size="6",
            margin_bottom="4",
            color=rx.color("gray", 12),
            id="response-time"
        ),
        
        rx.text(
            "I typically respond to messages within 24-48 hours. For urgent matters, please mention it in your message and I'll prioritize accordingly.",
            size="3",
            color=rx.color("gray", 10),
            line_height="1.7",
            margin_bottom="4"
        ),
        
        rx.hstack(
            rx.badge("📧 Email: 24hrs", variant="soft", color_scheme="blue"),
            rx.badge("💼 LinkedIn: 24hrs", variant="soft", color_scheme="blue"),
            rx.badge("💬 Discord: 2-6hrs", variant="soft", color_scheme="green"),
            spacing="2",
            wrap="wrap"
        ),
        
        align_items="start",
        width="100%",
        margin_top="8"
    )


def contact():
    """Contact page with multiple contact methods and form."""
    
    # Define sections for "On this page" navigation
    page_sections = [
        {"title": "Overview", "href": "#overview"},
        {"title": "Contact Methods", "href": "#contact-methods"},
        {"title": "Send Message", "href": "#contact-form"},
        {"title": "Response Time", "href": "#response-time"}
    ]
    
    # Page content
    content = rx.vstack(
        contact_intro(),
        contact_methods(),
        contact_form(),
        response_time(),
        spacing="9",
        align_items="start",
        width="100%"
    )
    
    return page_layout(
        content=content,
        title="Contact",
        on_page_sections=page_sections,
        max_width="4xl"
    )
