"""Blog data models for the Reflex blog system."""

from datetime import datetime
from typing import List
from pydantic import BaseModel


class BlogPost(BaseModel):
    """Model representing a blog post with frontmatter data."""

    title: str
    description: str
    last_modified: str
    tags: List[str]
    featured: bool = False
    published: bool = True
    date: str
    author: str = ""
    excerpt: str = ""
    content: str = ""
    file_path: str = ""
    tag_display: List[str]  # Pre-formatted tag display string

    @property
    def formatted_date(self) -> str:
        """Format the date for display, trying multiple date formats."""
        # Try to use the date field first, then fall back to last_modified
        date_str = self.date if self.date else self.last_modified

        if not date_str:
            return ""

        # Try multiple date formats
        formats_to_try = [
            "%Y-%m-%d",  # 2024-12-15
            "%d.%m.%Y",  # 15.12.2024
            "%m/%d/%Y",  # 12/15/2024
            "%B %d, %Y",  # December 15, 2024
        ]

        for fmt in formats_to_try:
            try:
                date_obj = datetime.strptime(date_str, fmt)
                return date_obj.strftime("%B %d, %Y")
            except ValueError:
                continue

        # If no format works, return the original string
        return date_str
