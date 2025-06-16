# site/components/live_clock.py
import reflex as rx
import asyncio
from datetime import datetime

class ClockState(rx.State):
    """State for the live clock widget."""
    current_time: str = datetime.now().strftime("%H:%M:%S")
    current_date: str = datetime.now().strftime("%B %d, %Y")
    is_running: bool = False

    @rx.event
    def update_time(self):
        """Update the current time."""
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        self.current_date = now.strftime("%B %d, %Y")

    @rx.event(background=True)
    async def start_clock(self):
        """Start the live clock updates."""
        async with self:
            if self.is_running:
                return
            self.is_running = True
            
        while True:
            async with self:
                if not self.is_running:
                    break
                now = datetime.now()
                self.current_time = now.strftime("%H:%M:%S")
                self.current_date = now.strftime("%B %d, %Y")
            
            await asyncio.sleep(1)  # Update every second
            
    @rx.event
    def stop_clock(self):
        """Stop the live clock updates."""
        self.is_running = False

def LiveClockWidget():
    """A compact live clock widget with current time and date."""
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading("🕐 Time", size="3"),  # Smaller heading
                rx.spacer(),
                rx.cond(
                    ClockState.is_running,
                    rx.icon_button(
                        rx.icon("pause", size=14),  # Smaller icon
                        on_click=ClockState.stop_clock,
                        variant="ghost",
                        size="1",  # Smaller button
                        aria_label="Stop clock"
                    ),
                    rx.icon_button(
                        rx.icon("play", size=14),  # Smaller icon
                        on_click=ClockState.start_clock,
                        variant="ghost", 
                        size="1",  # Smaller button
                        aria_label="Start clock"
                    )
                ),
                align_items="center",
                width="100%"
            ),
            rx.vstack(
                rx.text(
                    ClockState.current_time,
                    size="5",  # Smaller time display
                    weight="bold",
                    style={
                        "font_variant_numeric": "tabular-nums",
                        "letter_spacing": "0.05em"
                    }
                ),
                rx.text(
                    ClockState.current_date,
                    size="2",  # Smaller date
                    color_scheme="gray"
                ),
                align_items="center",
                spacing="1"  # Reduced spacing
            ),
            rx.cond(
                ClockState.is_running,
                rx.badge("Live", variant="soft", color_scheme="green", size="1"),
                rx.badge("Stopped", variant="soft", color_scheme="gray", size="1")
            ),
            align_items="center",
            spacing="2",  # Reduced overall spacing
            padding="1rem"  # Reduced padding
        ),
        width="100%",
        height="auto",  # Let content determine height
        on_mount=ClockState.start_clock
    )
