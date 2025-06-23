# site/components/live_clock.py
import reflex as rx
from retest.site.state import ClockState


def LiveClockWidget():
    """A compact live clock widget with current time and date."""
    return rx.card(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.heading("🕐 Time", size="3"),
                    rx.spacer(),
                    rx.cond(
                        ClockState.is_running,
                        rx.icon_button(
                            rx.icon("pause", size=14),
                            on_click=ClockState.stop_clock,
                            variant="ghost",
                            size="1",
                            aria_label="Stop clock",
                        ),
                        rx.icon_button(
                            rx.icon("play", size=14),
                            on_click=ClockState.start_clock,
                            variant="ghost",
                            size="1",
                            aria_label="Start clock",
                        ),
                    ),
                    align_items="center",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        ClockState.current_time,
                        size="5",
                        weight="bold",
                        style={
                            "font_variant_numeric": "tabular-nums",
                            "letter_spacing": "0.05em",
                        },
                    ),
                    rx.text(
                        ClockState.current_date,
                        size="2",
                        color_scheme="gray",
                    ),
                    align_items="center",
                    spacing="1",
                ),
                rx.cond(
                    ClockState.is_running,
                    rx.badge("Live", variant="soft", color_scheme="green", size="1"),
                    rx.badge("Stopped", variant="soft", color_scheme="gray", size="1"),
                ),
                align_items="center",
                spacing="2",
                padding="1rem",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.hstack(
                    rx.heading("🕐 Time", size="2"),
                    rx.spacer(),
                    rx.cond(
                        ClockState.is_running,
                        rx.icon_button(
                            rx.icon("pause", size=12),
                            on_click=ClockState.stop_clock,
                            variant="ghost",
                            size="1",
                            aria_label="Stop clock",
                        ),
                        rx.icon_button(
                            rx.icon("play", size=12),
                            on_click=ClockState.start_clock,
                            variant="ghost",
                            size="1",
                            aria_label="Start clock",
                        ),
                    ),
                    align_items="center",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        ClockState.current_time,
                        size="4",
                        weight="bold",
                        style={
                            "font_variant_numeric": "tabular-nums",
                            "letter_spacing": "0.05em",
                        },
                    ),
                    rx.text(
                        ClockState.current_date,
                        size="1",
                        color_scheme="gray",
                    ),
                    align_items="center",
                    spacing="1",
                ),
                rx.cond(
                    ClockState.is_running,
                    rx.badge("Live", variant="soft", color_scheme="green", size="1"),
                    rx.badge("Stopped", variant="soft", color_scheme="gray", size="1"),
                ),
                align_items="center",
                spacing="2",
                padding="0.5rem",
            )
        ),
        width="100%",
        height="auto",
        on_mount=ClockState.start_clock,
    )
