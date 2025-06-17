# site/components/about_contact.py
import reflex as rx
from retest.site.state import DiscordAvatarState, ContactState


def AboutSection():
    return rx.vstack(
        rx.heading("About Me", size="5", margin_bottom="0.5em"),
        rx.text(
            "Hello! I'm a hobby developer, mostly coding in Python. I don't have much web dev experience, "
            "so I'm really trying my best to make things user-friendly, the site is a work in progress. "
            "This dashboard is a place to showcase some of my projects and experiments. "
            "I enjoy learning and exploring new technologies like Reflex!",
            line_height="1.6",
            color_scheme="gray",
        ),
        rx.text(
            "Write me directly at ",
            rx.link(
                "alex@alexdot.me",
                href="mailto:alex@alexdot.me",
                color_scheme="blue",
                style={"text_decoration": "underline"},
            ),
            line_height="1.6",
            color_scheme="gray",
            margin_top="0.5rem",
        ),
        rx.hstack(
            rx.skeleton(
                rx.avatar(
                    fallback="A",
                    src=DiscordAvatarState.avatar_url,
                    size="6",
                    radius="full",
                ),
                loading=DiscordAvatarState.loading,
            ),
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.icon_button(
                            rx.icon("github"),
                            variant="ghost",
                            size="2",
                            aria_label="GitHub",
                        ),
                        href="https://github.com/unfortunatelyalex",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon_button(
                            rx.icon("linkedin"),
                            variant="ghost",
                            size="2",
                            aria_label="LinkedIn",
                        ),
                        href="#",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon_button(
                            rx.icon("twitter"),
                            variant="ghost",
                            size="2",
                            aria_label="Twitter",
                        ),
                        href="#",
                        is_external=True,
                    ),
                    spacing="2",
                ),
                rx.button(
                    rx.icon("download", size=16),
                    "Download CV",
                    variant="outline",
                    size="2",
                    on_click=rx.toast.info(
                        "CV download is not implemented yet.",
                        duration=3000,
                    ),
                    # rx.download(
                    #         url="/cv.pdf", filename="Alex_CV.pdf")
                ),
                align_items="start",
                spacing="3",
            ),
            align_items="center",
            spacing="4",
            margin_top="1rem",
        ),
        align_items="start",
        spacing="3",
        width="100%",
        height="100%",
    )


def ContactSection():
    return rx.card(
        rx.vstack(
            rx.heading("Get in Touch", size="5", margin_bottom="0.5em"),
            rx.cond(
                ContactState.submit_success,
                rx.vstack(
                    rx.callout(
                        "Thanks! I'll get back to you soon.",
                        icon="check",
                        color_scheme="green",
                        margin_bottom="1rem",
                    ),
                    rx.button(
                        "Send Another Message",
                        on_click=ContactState.reset_form,
                        variant="outline",
                        size="3",
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.vstack(
                    # Name and Email fields horizontally next to each other
                    rx.hstack(
                        # Name field with validation
                        rx.vstack(
                            rx.input(
                                value=ContactState.name,
                                on_blur=ContactState.validate_name,
                                on_change=ContactState.set_name,
                                placeholder="Your name",
                                size="3",
                            ),
                            rx.cond(
                                ContactState.name_error != "",
                                rx.text(
                                    ContactState.name_error,
                                    size="1",
                                    color_scheme="red",
                                ),
                            ),
                            spacing="1",
                            width="100%",
                        ),
                        # Email field with validation
                        rx.vstack(
                            rx.input(
                                type="email",
                                value=ContactState.email,
                                on_blur=ContactState.validate_email,
                                on_change=ContactState.set_email,
                                placeholder="Your email",
                                size="3",
                            ),
                            rx.cond(
                                ContactState.email_error != "",
                                rx.text(
                                    ContactState.email_error,
                                    size="1",
                                    color_scheme="red",
                                ),
                            ),
                            spacing="1",
                            width="100%",
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    # Message field with validation
                    rx.vstack(
                        rx.text_area(
                            value=ContactState.message,
                            on_blur=ContactState.validate_message,
                            on_change=ContactState.set_message,
                            placeholder="Your message",
                            rows="4",
                            resize="vertical",
                        ),
                        rx.cond(
                            ContactState.message_error != "",
                            rx.text(
                                ContactState.message_error, size="1", color_scheme="red"
                            ),
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    # Submit button with loading state
                    rx.button(
                        rx.cond(
                            ContactState.is_submitting,
                            rx.hstack(
                                rx.spinner(size="1"),
                                rx.text("Sending..."),
                                align_items="center",
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.icon("send", size=16),
                                rx.text("Send Message"),
                                align_items="center",
                                spacing="2",
                            ),
                        ),
                        on_click=ContactState.send_message,
                        size="3",
                        loading=ContactState.is_submitting,
                        style={
                            "_hover": {
                                "transform": "translateY(-1px)",
                                "box-shadow": "0 4px 12px rgba(0,0,0,0.15)",
                            }
                        },
                    ),
                    spacing="3",
                    width="100%",
                ),
            ),
            rx.divider(),
            rx.hstack(
                rx.text("Or reach me directly:", size="2", color_scheme="gray"),
                rx.link(
                    "alex@alexdot.me",
                    href="mailto:alex@alexdot.me",
                    color_scheme="blue",
                ),
                align_items="center",
                spacing="2",
            ),
            align_items="start",
            spacing="3",
        ),
        width="100%",
        height="100%",
    )
