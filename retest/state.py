"""State management for the portfolio site."""

import reflex as rx
from typing import Dict, List, Union, Any
from .utils.blog import load_all_blog_posts


class NavigationState(rx.State):
    """State for managing navigation and UI interactions."""

    # Sidebar state
    sidebar_collapsed: bool = False
    current_page: str = "about"

    # Theme state
    theme_mode: str = "auto"  # light, dark, auto

    # Mobile navigation
    mobile_menu_open: bool = False

    # Current page sections for "On this page" navigation
    current_sections: List[Dict[str, str]] = []

    def toggle_sidebar(self):
        """Toggle sidebar collapse state."""
        self.sidebar_collapsed = not self.sidebar_collapsed

    def toggle_mobile_menu(self):
        """Toggle mobile menu state."""
        self.mobile_menu_open = not self.mobile_menu_open

    def set_current_page(self, page: str):
        """Set the current page."""
        self.current_page = page
        self.mobile_menu_open = False  # Close mobile menu when navigating

    def set_theme_mode(self, mode: str):
        """Set theme mode (light, dark, auto)."""
        self.theme_mode = mode
        # Note: Theme switching will be handled in the frontend component

    def set_page_sections(self, sections: List[Dict[str, str]]):
        """Set sections for current page navigation."""
        self.current_sections = sections


class PortfolioState(rx.State):
    """State for portfolio-specific data."""

    # Personal info
    name: str = "Alex"
    title: str = "Hobby dev"
    bio: str = (
        "Hobby developer creating sloppy solutions with partially modern technologies."
    )

    # Contact info
    email: str = "alex@alexdot.me"
    github_url: str = "https://github.com/unfortunatelyalex"
    linkedin_url: str = "https://linkedin.com/in/alexander-bonin-2758b5178/"

    # Projects data
    projects: List[Dict[str, str]] = [
        {
            "id": "project-alex-site",
            "name": "project alex.",
            "description": "A simple portfolio website built with pure HTML, CSS, and JavaScript.",
            "tech_stack": "HTML, CSS, JS",
            "github_url": "",
            "demo_url": "https://alexdot.me/",
            "status": "completed",
        },
        {
            "id": "project-beta",
            "name": "Project Beta",
            "description": "Mobile-first responsive dashboard for data visualization.",
            "tech_stack": "TypeScript, Vue.js, D3.js",
            "github_url": "https://github.com/username/project-beta",
            "demo_url": "",
            "status": "in-progress",
        },
    ]

    # Skills data
    skills: Dict[str, List[str]] = {
        "Languages": ["Python"],
        "Frameworks": ["Reflex"],
        "Tools": ["Docker", "Git", "VS Code"],
    }

    # Blog posts data - loaded from markdown files
    _blog_posts: List[Dict[str, Union[str, List[str]]]] = []
    _blog_posts_loaded: bool = False

    @rx.var
    def blog_posts(self) -> List[Dict[str, Union[str, List[str]]]]:
        """Get blog posts, loading them if necessary."""
        if not self._blog_posts_loaded:
            try:
                self._blog_posts = load_all_blog_posts()
                self._blog_posts_loaded = True
            except Exception as e:
                print(f"Error loading blog posts: {e}")
                self._blog_posts = []
        return self._blog_posts

    def load_blog_posts(self):
        """Load blog posts from markdown files."""
        if not self._blog_posts_loaded:
            try:
                self._blog_posts = load_all_blog_posts()
                self._blog_posts_loaded = True
            except Exception as e:
                print(f"Error loading blog posts: {e}")
                # Fallback to empty list if loading fails
                self._blog_posts = []

    def get_blog_posts(self) -> List[Dict[str, Union[str, List[str]]]]:
        """Get blog posts, loading them if necessary."""
        if not self._blog_posts_loaded:
            self.load_blog_posts()
        return self._blog_posts
