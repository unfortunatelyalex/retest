"""Style configuration for the portfolio website."""
import reflex as rx

# Color scheme
COLORS = {
    # Light mode colors
    "light": {
        "bg_primary": "#ffffff",
        "bg_secondary": "#f8f9fa", 
        "text_primary": "#333333",
        "text_secondary": "#666666",
        "border": "#e5e5e5",
        "code_bg": "#f4f4f4",
        "accent": "#007ACC",
        "sidebar_bg": "#fdfdfd",
        "header_bg": "#ffffff",
    },
    # Dark mode colors  
    "dark": {
        "bg_primary": "#0a0a0a",
        "bg_secondary": "#1a1a1a",
        "text_primary": "#eaeaea", 
        "text_secondary": "#b0b0b0",
        "border": "#333333",
        "code_bg": "#2a2a2a",
        "accent": "#007ACC",
        "sidebar_bg": "#111111",
        "header_bg": "#0a0a0a",
    }
}

# Typography
FONTS = {
    "body": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
    "heading": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
    "mono": "'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace",
}

# Breakpoints
BREAKPOINTS = {
    "mobile": "48em",  # 768px
    "tablet": "62em",  # 992px  
    "desktop": "80em", # 1280px
}

# Layout dimensions
LAYOUT = {
    "sidebar_width": "280px",
    "sidebar_collapsed_width": "60px",
    "header_height": "60px",
    "max_content_width": "1200px",
}

# Common styles
def get_base_styles():
    """Get base styles for the app."""
    return {
        "font_family": FONTS["body"],
        "color": rx.color("gray", 12),
        "background_color": rx.color("gray", 1),
        "line_height": "1.6",
    }

def get_heading_styles(size: str = "6"):
    """Get heading styles."""
    return {
        "font_family": FONTS["heading"],
        "font_weight": "600",
        "color": rx.color("gray", 12),
        "line_height": "1.2",
        "size": size,
    }

def get_code_styles():
    """Get code block styles."""
    return {
        "font_family": FONTS["mono"],
        "background_color": rx.color("gray", 3),
        "border": f"1px solid {rx.color('gray', 4)}",
        "border_radius": "8px",
        "padding": "1rem",
        "overflow_x": "auto",
        "font_size": "0.9rem",
        "line_height": "1.5",
    }

def get_tip_styles():
    """Get tip/note panel styles."""
    return {
        "background_color": rx.color("blue", 2),
        "border_left": f"4px solid {rx.color('blue', 6)}",
        "padding": "1rem",
        "border_radius": "0 8px 8px 0",
        "margin": "1rem 0",
        "font_style": "italic",
        "color": rx.color("blue", 11),
    }

def get_sidebar_styles():
    """Get sidebar styles."""
    return {
        "background_color": rx.color("gray", 2),
        "border_right": f"1px solid {rx.color('gray', 4)}",
        "height": "100vh",
        "position": "fixed",
        "left": "0",
        "top": "0",
        "z_index": "1000",
        "overflow_y": "auto",
        "transition": "width 0.3s ease",
    }

def get_header_styles():
    """Get header styles.""" 
    return {
        "background_color": rx.color("gray", 1),
        "border_bottom": f"1px solid {rx.color('gray', 4)}",
        "height": LAYOUT["header_height"],
        "position": "fixed",
        "top": "0",
        "right": "0",
        "z_index": "999",
        "padding": "0 1rem",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
    }

def get_content_styles():
    """Get main content area styles."""
    return {
        "margin_left": LAYOUT["sidebar_width"],
        "margin_top": LAYOUT["header_height"], 
        "padding": "2rem",
        "min_height": f"calc(100vh - {LAYOUT['header_height']})",
        "max_width": LAYOUT["max_content_width"],
        "transition": "margin-left 0.3s ease",
    }

def get_link_styles():
    """Get link styles."""
    return {
        "color": rx.color("blue", 9),
        "text_decoration": "none",
        "_hover": {
            "color": rx.color("blue", 10),
            "text_decoration": "underline",
        },
    }

def get_button_styles(variant: str = "solid"):
    """Get button styles."""
    if variant == "ghost":
        return {
            "background_color": "transparent",
            "color": rx.color("gray", 11),
            "border": "none",
            "_hover": {
                "background_color": rx.color("gray", 3),
            },
        }
    return {
        "background_color": rx.color("blue", 9),
        "color": "white",
        "border": "none",
        "border_radius": "6px",
        "padding": "0.5rem 1rem",
        "_hover": {
            "background_color": rx.color("blue", 10),
        },
    }
