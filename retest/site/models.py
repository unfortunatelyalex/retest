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
    date: str = ""
    author: str = ""
    excerpt: str = ""
    content: str = ""
    file_path: str = ""

    @property
    def formatted_date(self) -> str:
        """Format the last_modified date for display."""
        try:
            date_obj = datetime.strptime(self.last_modified, "%Y-%m-%d")
            return date_obj.strftime("%B %d, %Y")
        except ValueError:
            return self.last_modified

    @property
    def tag_display(self) -> str:
        """Join tags for display."""
        return ", ".join(self.tags[:3])  # Show first 3 tags
