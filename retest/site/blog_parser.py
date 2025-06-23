"""Blog frontmatter parser for markdown files."""

from typing import List, Optional
from pathlib import Path
import frontmatter
from .models import BlogPost


class BlogParser:
    """Parser for blog posts with frontmatter."""

    def __init__(self, blog_posts_dir: str):
        self.blog_posts_dir = Path(blog_posts_dir)

    def load_blog_post(self, file_path: Path) -> Optional[BlogPost]:
        """Load a single blog post from a markdown file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            metadata = post.metadata

            # Extract required fields with type conversion
            title = str(metadata.get("title", file_path.stem.replace("-", " ").title()))
            description = str(metadata.get("description", metadata.get("excerpt", "")))
            last_modified = str(metadata.get("last_modified", ""))

            # Handle tags - ensure it's a list of strings
            tags_raw = metadata.get("tags", [])
            if isinstance(tags_raw, list):
                tags = [str(tag) for tag in tags_raw]
            else:
                tags = []

            featured = bool(metadata.get("featured", False))
            published = bool(metadata.get("published", True))

            # Optional fields
            date_val = metadata.get("date", "")
            date = str(date_val) if date_val else ""

            author_val = metadata.get("author", "")
            author = str(author_val) if author_val else ""

            excerpt_val = metadata.get("excerpt", "")
            excerpt = str(excerpt_val) if excerpt_val else ""

            return BlogPost(
                title=title,
                description=description,
                last_modified=last_modified,
                tags=tags,
                featured=featured,
                published=published,
                date=date,
                author=author,
                excerpt=excerpt,
                content=post.content,
                file_path=str(file_path),
            )

        except Exception as e:
            print(f"Error loading blog post {file_path}: {e}")
            return None

    def load_all_posts(self) -> List[BlogPost]:
        """Load all blog posts from the blog posts directory."""
        posts = []

        if not self.blog_posts_dir.exists():
            print(f"Blog posts directory does not exist: {self.blog_posts_dir}")
            return posts

        for file_path in self.blog_posts_dir.glob("*.md"):
            post = self.load_blog_post(file_path)
            if post and post.published:  # Only include published posts
                posts.append(post)

        # Sort by last_modified date (newest first)
        posts.sort(key=lambda x: x.last_modified, reverse=True)

        return posts

    def get_featured_posts(self) -> List[BlogPost]:
        """Get only featured blog posts."""
        all_posts = self.load_all_posts()
        return [post for post in all_posts if post.featured]

    def get_posts_by_tag(self, tag: str) -> List[BlogPost]:
        """Get blog posts filtered by a specific tag."""
        all_posts = self.load_all_posts()
        return [
            post for post in all_posts if tag.lower() in [t.lower() for t in post.tags]
        ]


# Create a global instance
blog_parser = BlogParser("/home/alex/retest/retest/public/blog_posts")
