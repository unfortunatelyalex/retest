# site/components/progress_bar.py
import reflex as rx

def progress_bar(progress: int = 0) -> rx.Component:
    """Simple animated progress bar for music playback"""
    return rx.box(
        rx.box(
            width=f"{progress}%",
            height="100%",
            background_color=rx.color("blue", 9),
            border_radius="full",
            style={
                "transition": "width 0.3s ease-in-out",
                "animation": "pulse 2s infinite" if progress > 0 else None
            }
        ),
        width="100%",
        height="4px",
        background_color=rx.color("gray", 4),
        border_radius="full",
        overflow="hidden"
    )

def music_visualizer() -> rx.Component:
    """Simple music visualizer bars"""
    return rx.hstack(
        *[rx.box(
            width="3px",
            background_color=rx.color("blue", 8),
            border_radius="full",
            style={
                "height": f"{15 + (i * 5)}px",
                "animation": f"pulse {1 + (i * 0.2)}s infinite alternate"
            }
        ) for i in range(5)],
        spacing="1",
        align_items="end"
    )
