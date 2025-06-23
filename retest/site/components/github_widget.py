"""GitHub contribution chart component - displays a GitHub-style contribution graph."""

import reflex as rx
from datetime import datetime
from retest.site.state import GitHubState, TooltipState


def real_contribution_grid() -> rx.Component:
    """Real contribution grid using actual GitHub data."""
    # Define theme-aware colors
    light_colors = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    dark_colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    def format_tooltip(day):
        # Parse date string (YYYY-MM-DD)
        try:
            dt = datetime.strptime(day["date"], "%Y-%m-%d")
            day_num = dt.day
            # Suffix logic
            if 10 <= day_num % 100 <= 20:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(day_num % 10, "th")
            month = dt.strftime("%B")
            count = day["count"]
            count_str = f"{count} contribution" if count == 1 else f"{count} contributions"
            return f"{count_str} on {month} {day_num}{suffix}."
        except Exception:
            # Fallback to old format
            return f"{day['count']} contributions on {day['date']}"

    return rx.cond(
        GitHubState.contribution_weeks != [],
        rx.flex(
            rx.foreach(
                GitHubState.contribution_weeks,
                lambda week: rx.flex(
                    rx.foreach(
                        week,
                        lambda day: rx.tooltip(
                            rx.box(
                                width="11px",
                                height="11px",
                                background_color=rx.color_mode_cond(
                                    light=rx.cond(
                                        day["level"] == 0,
                                        light_colors[0],
                                        rx.cond(
                                            day["level"] == 1,
                                            light_colors[1],
                                            rx.cond(
                                                day["level"] == 2,
                                                light_colors[2],
                                                rx.cond(
                                                    day["level"] == 3,
                                                    light_colors[3],
                                                    light_colors[4],
                                                ),
                                            ),
                                        ),
                                    ),
                                    dark=rx.cond(
                                        day["level"] == 0,
                                        dark_colors[0],
                                        rx.cond(
                                            day["level"] == 1,
                                            dark_colors[1],
                                            rx.cond(
                                                day["level"] == 2,
                                                dark_colors[2],
                                                rx.cond(
                                                    day["level"] == 3,
                                                    dark_colors[3],
                                                    dark_colors[4],
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                                border_radius="2px",
                                border=rx.color_mode_cond(
                                    light="1px solid rgba(27, 31, 36, 0.06)",
                                    dark="1px solid rgba(48, 54, 61, 0.2)",
                                ),
                                margin="1px",
                                cursor="pointer",
                                style={"user-select": "none"},
                                on_click=lambda: TooltipState.open_tooltip(day["date"]),
                                _hover={
                                    "border": rx.color_mode_cond(
                                        light="1px solid rgba(27, 31, 36, 0.3)",
                                        dark="1px solid rgba(240, 246, 252, 0.3)",
                                    ),
                                    "outline": "2px solid rgba(58, 115, 214, 0.4)",
                                    "outline_offset": "-1px",
                                },
                            ),
                            content=format_tooltip(day),
                            open=(TooltipState.open_day == day["date"]),
                            on_open_change=lambda value: TooltipState.close_tooltip(
                                value, day["date"]
                            ),
                            align="center",
                        ),
                    ),
                    direction="column",
                    gap="1px",
                ),
            ),
            direction="row",
            gap="2px",
            wrap="nowrap",
            width="689px",
        ),
        # Fallback sample grid when no data
        # sample_contribution_grid()
    )


def static_month_labels() -> rx.Component:
    """Static month labels showing last 12 months from current date."""
    # Calculate the last 12 months
    current_date = datetime.now()
    months = []

    for i in range(12):
        # Go back i months from current date
        if current_date.month - i <= 0:
            month_date = current_date.replace(
                year=current_date.year - 1, month=current_date.month - i + 12
            )
        else:
            month_date = current_date.replace(month=current_date.month - i)
        months.insert(0, month_date.strftime("%b").lower())

    return rx.flex(
        *[
            rx.text(
                month.capitalize(),
                font_size="12px",
                color=rx.color_mode_cond(
                    light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
                ),
                font_weight="400",
                flex="1",  # Equal space for each month
                text_align="left",
            )
            for i, month in enumerate(months)
        ],
        width="100%",
        justify="between",  # Spread labels evenly
        align="start",
        margin_bottom="8px",
    )


def sample_contribution_grid() -> rx.Component:
    """Sample contribution grid when real data is not available."""
    # Create GitHub's dynamic contribution grid (53 weeks = 371 days)
    weeks = 53
    days_per_week = 7

    # GitHub's contribution colors adapted for light/dark mode
    light_colors = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    dark_colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    weeks_components = []
    for week in range(weeks):
        week_cells = []
        for day in range(days_per_week):
            # Create a simple pattern for demonstration
            level = (week + day) % 5

            week_cells.append(
                rx.box(
                    width="11px",
                    height="11px",
                    background_color=rx.color_mode_cond(
                        light=light_colors[level], dark=dark_colors[level]
                    ),
                    border_radius="2px",
                    border=rx.color_mode_cond(
                        light="1px solid rgba(27, 31, 36, 0.06)",
                        dark="1px solid rgba(48, 54, 61, 0.2)",
                    ),
                    margin="1px",
                    cursor="pointer",
                    _hover={
                        "border": rx.color_mode_cond(
                            light="1px solid rgba(27, 31, 36, 0.3)",
                            dark="1px solid rgba(240, 246, 252, 0.3)",
                        ),
                        "outline": "2px solid rgba(58, 115, 214, 0.4)",
                        "outline_offset": "-1px",
                    },
                )
            )

        weeks_components.append(rx.flex(*week_cells, direction="column", gap="1px"))

    return rx.flex(
        *weeks_components,
        direction="row",
        gap="2px",
        wrap="nowrap",
        width="689px",  # Fixed width to match month labels
    )


def dynamic_month_labels() -> rx.Component:
    """Render non-overlapping month labels like GitHub."""
    return rx.cond(
        GitHubState.months != [],
        rx.flex(
            rx.foreach(
                GitHubState.months,
                lambda month: rx.text(
                    month["name"],
                    font_size="12px",
                    color=rx.color_mode_cond(
                        light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
                    ),
                    font_weight="400",
                    text_align="left",
                    white_space="nowrap",
                    position="absolute",
                    left=f"calc({month['week_index']} * 15px)",
                ),
            ),
            width="689px",  # 53 weeks * 13px + 52 gaps * 2px = 689px
            height="16px",
            position="relative",
            margin_bottom="1px",
        ),
    )


def day_labels_static() -> rx.Component:
    """Static day labels."""
    return rx.vstack(
        rx.text("", height="11px", width="25px"),  # Sunday spacer
        rx.text(
            "Mon",
            font_size="11px",
            color=rx.color_mode_cond(
                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
            ),
            width="25px",
        ),
        rx.text("", height="11px", width="25px"),  # Tuesday spacer
        rx.text(
            "Wed",
            font_size="11px",
            color=rx.color_mode_cond(
                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
            ),
            width="25px",
        ),
        rx.text("", height="11px", width="25px"),  # Thursday spacer
        rx.text(
            "Fri",
            font_size="11px",
            color=rx.color_mode_cond(
                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
            ),
            width="25px",
        ),
        rx.text("", height="11px", width="25px"),  # Saturday spacer
        gap="0px",
        margin_right="8px",
        align_items="flex-start",  # vstack uses align_items for cross-axis alignment
    )


def contribution_legend() -> rx.Component:
    """Legend showing contribution levels."""
    return rx.flex(
        rx.text(
            "Less",
            font_size="12px",
            color=rx.color_mode_cond(
                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
            ),
            margin_right="4px",
        ),
        *[
            rx.box(
                width="11px",
                height="11px",
                background_color=rx.color_mode_cond(
                    light=["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"][i],
                    dark=["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"][i],
                ),
                border_radius="2px",
                border=rx.color_mode_cond(
                    light="1px solid rgba(27, 31, 36, 0.06)",
                    dark="1px solid rgba(48, 54, 61, 0.2)",
                ),
                margin="1px",
            )
            for i in range(5)
        ],
        rx.text(
            "More",
            font_size="12px",
            color=rx.color_mode_cond(
                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
            ),
            margin_left="4px",
        ),
        align="center",
        gap="2px",
        margin_top="2px",
    )


def contribution_chart() -> rx.Component:
    """Main GitHub contribution chart component."""
    return rx.box(
        # Loading state
        rx.cond(
            GitHubState.is_loading,
            rx.flex(
                rx.spinner(size="3"),
                rx.text(
                    "Loading contributions...",
                    color=rx.color_mode_cond(
                        light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
                    ),
                ),
                align="center",
                gap="2",
                justify="center",
                height="140px",
            ),
            # Error state
            rx.cond(
                GitHubState.error_message != "",
                rx.flex(
                    rx.text(
                        GitHubState.error_message,
                        color=rx.color_mode_cond(
                            light="rgb(218, 54, 51)", dark="rgb(248, 81, 73)"
                        ),
                        font_size="14px",
                    ),
                    align="center",
                    justify="center",
                    height="140px",
                ),
                # Chart content
                rx.flex(
                    # Fixed left side with day labels
                    rx.flex(
                        # Empty spacer for month labels row
                        rx.box(width="25px", height="16px", margin_bottom="7px"),
                        # Day labels
                        day_labels_static(),
                        # Empty spacer for legend row
                        rx.box(width="25px", height="16px", margin_top="14px"),
                        direction="column",
                        align="start",
                        flex_shrink="0",  # Prevent shrinking
                    ),
                    # Scrollable container for month labels, contribution grid, and legend
                    rx.box(
                        rx.flex(
                            # Month labels
                            dynamic_month_labels(),
                            # Contribution grid
                            real_contribution_grid(),
                            # Legend (moved into scrollable area)
                            contribution_legend(),
                            direction="column",
                            gap="6px",
                            align="start",
                        ),
                        overflow_x="auto",
                        overflow_y="hidden",
                        width="100%",
                        margin_left="8px",
                    ),
                    direction="row",
                    align="start",
                    gap="0",
                ),
            ),
        ),
        padding="16px",
        background=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.95)", dark="rgba(13, 17, 23, 0.95)"
        ),
        border_radius="8px",
        border=rx.color_mode_cond(
            light="1px solid rgba(27, 31, 36, 0.15)",
            dark="1px solid rgba(48, 54, 61, 0.2)",
        ),
        width="100%",
        overflow="visible",
    )


def github_contribution_widget() -> rx.Component:
    """Complete GitHub contribution widget with controls."""
    return rx.box(
        rx.desktop_only(
            rx.flex(
                rx.flex(
                    rx.cond(
                        GitHubState.avatar_url != "",
                        rx.image(
                            src=GitHubState.avatar_url,
                            width="24px",
                            height="24px",
                            border_radius="50%",
                            border=rx.color_mode_cond(
                                light="1px solid rgba(27, 31, 36, 0.15)",
                                dark="1px solid rgba(48, 54, 61, 0.2)",
                            ),
                        ),
                        rx.box(),
                    ),
                    rx.flex(
                        rx.link(
                            f"@{GitHubState.github_username}",
                            href=f"https://github.com/{GitHubState.github_username}",
                            font_weight="600",
                            color=rx.color_mode_cond(
                                light="rgb(31, 35, 40)", dark="rgb(201, 209, 217)"
                            ),
                        ),
                        rx.text(
                            f"{GitHubState.total_contributions} contributions in the last year",
                            font_size="14px",
                            color=rx.color_mode_cond(
                                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
                            ),
                        ),
                        direction="column",
                        gap="2px",
                    ),
                    align="center",
                    gap="8px",
                ),
                align="center",
                margin_bottom="16px",
            )
        ),
        rx.mobile_and_tablet(
            rx.flex(
                rx.flex(
                    rx.cond(
                        GitHubState.avatar_url != "",
                        rx.image(
                            src=GitHubState.avatar_url,
                            width="20px",
                            height="20px",
                            border_radius="50%",
                            border=rx.color_mode_cond(
                                light="1px solid rgba(27, 31, 36, 0.15)",
                                dark="1px solid rgba(48, 54, 61, 0.2)",
                            ),
                        ),
                        rx.box(),
                    ),
                    rx.flex(
                        rx.link(
                            f"@{GitHubState.github_username}",
                            href=f"https://github.com/{GitHubState.github_username}",
                            font_weight="600",
                            color=rx.color_mode_cond(
                                light="rgb(31, 35, 40)", dark="rgb(201, 209, 217)"
                            ),
                        ),
                        rx.text(
                            f"{GitHubState.total_contributions} contributions in the last year",
                            font_size="12px",
                            color=rx.color_mode_cond(
                                light="rgb(101, 109, 118)", dark="rgb(125, 128, 141)"
                            ),
                        ),
                        direction="column",
                        gap="2px",
                    ),
                    align="center",
                    gap="6px",
                ),
                align="center",
                margin_bottom="12px",
            )
        ),
        # Contribution chart
        contribution_chart(),
        width="100%",
        padding="20px",
        background=rx.color_mode_cond(
            light="linear-gradient(135deg, rgba(246, 248, 250, 0.9), rgba(255, 255, 255, 0.8))",
            dark="linear-gradient(135deg, rgba(13, 17, 23, 0.9), rgba(22, 27, 34, 0.8))",
        ),
        border_radius="12px",
        border=rx.color_mode_cond(
            light="1px solid rgba(27, 31, 36, 0.15)",
            dark="1px solid rgba(48, 54, 61, 0.3)",
        ),
        box_shadow=rx.color_mode_cond(
            light="0 8px 32px rgba(31, 35, 40, 0.08)",
            dark="0 8px 32px rgba(0, 0, 0, 0.3)",
        ),
        backdrop_filter="blur(10px)",
    )


def github_widget() -> rx.Component:
    """Main GitHub widget function called from the dashboard."""
    return rx.skeleton(
        github_contribution_widget(),
        loading=rx.cond(GitHubState.chart_ready, False, True),
    )
