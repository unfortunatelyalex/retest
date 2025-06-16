# site/components/stats_widget.py
import reflex as rx

def CodingStatsWidget():
    stats = [
        {"label": "Python", "icon_tag": "code", "value": "70%", "progress": 70, "color": "blue"},
        {"label": "JavaScript", "icon_tag": "code", "value": "20%", "progress": 20, "color": "yellow"},
        {"label": "Others", "icon_tag": "binary", "value": "10%", "progress": 10, "color": "green"},
    ]
    
    project_stats = [
        {"label": " ", "icon_tag": "folder", "value": "12", "description": "Completed projects"},
        {"label": " ", "icon_tag": "calendar", "value": "5", "description": "Years of experience"},
    ]
    
    return rx.vstack(
        rx.heading("💻 Coding Stats", size="4", margin_bottom="0.5em"),
            
            # Programming languages with progress bars
            rx.vstack(
                rx.text("Languages", weight="medium", size="3", margin_bottom="0.5em"),
                *[rx.vstack(
                    rx.hstack(
                        rx.icon(tag=stat["icon_tag"], size=16),
                        rx.text(stat["label"], size="2"),
                        rx.spacer(),
                        rx.text(stat["value"], size="2", weight="medium"),
                        align_items="center",
                        width="100%"
                    ),
                    rx.progress(
                        value=stat["progress"],
                        color_scheme=stat["color"],
                        style={"width": "100%", "height": "4px"}
                    ),
                    spacing="1",
                    width="100%"
                ) for stat in stats],
                spacing="3",
                width="100%"
            ),
            
            rx.divider(),
            
            # Project stats
            rx.grid(
                *[rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(tag=stat["icon_tag"], size=20, color_scheme="blue"),
                            rx.vstack(
                                rx.text(stat["value"], size="5", weight="bold"),
                                rx.text(stat["label"], size="1", color_scheme="gray"),
                                align_items="start",
                                spacing="0"
                            ),
                            align_items="center",
                            spacing="2"
                        ),
                        rx.text(stat["description"], size="1", color_scheme="gray"),
                        align_items="center",
                        spacing="1"
                    ),
                    padding="1rem",
                    border_radius="md",
                    background_color=rx.color("gray", 2, alpha=True),
                    style={
                        "_hover": {
                            "background_color": rx.color("gray", 3, alpha=True),
                            "transition": "background-color 0.2s ease"
                        }
                    }
                ) for stat in project_stats],
                columns="2",
                gap="3",
                width="100%"
            ),
            
            align_items="start",
            spacing="4",
            width="100%",
            height="100%"
        )
