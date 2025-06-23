# site/blog_parser.py
import os
import glob
import frontmatter
from typing import Dict, List, Optional
from datetime import datetime
import re


class BlogPost:
    """Represents a single blog post with metadata and content."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.slug = os.path.splitext(self.filename)[0]

        # Load and parse the post
        self._load_post()

    def _load_post(self):
        """Load and parse the blog post from the file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)

            self.metadata = post.metadata
            self.content = post.content

            # Extract or set default values
            self._extract_metadata()

        except Exception as e:
            print(f"Error loading blog post {self.file_path}: {e}")
            # Set defaults if parsing fails
            self.metadata = {}
            self.content = ""
            self._extract_metadata()

    def _extract_metadata(self):
        """Extract and validate metadata, setting defaults where needed."""
        # Title - from frontmatter, first heading, or filename
        self.title = self.metadata.get("title")
        if not self.title:
            # Try to extract from first heading in content
            if self.content:
                lines = self.content.split("\n")
                for line in lines:
                    if line.strip().startswith("# "):
                        self.title = line.strip()[2:].strip()
                        break

            # Fallback to filename
            if not self.title:
                self.title = self.slug.replace("-", " ").replace("_", " ").title()

        # Date handling
        self.date = self._parse_date()
        self.lm_date = self._parse_last_modified_date()
        self.date_published = self.date  # Alias for compatibility
        self.last_modified = self.lm_date  # Use last modified date if available
        # self.last_modified = self.metadata.get("last_modified", "")

        # Extract excerpt
        self.excerpt = self._extract_excerpt()

        # Tags
        self.tags = self.metadata.get("tags", [])
        if isinstance(self.tags, str):
            # Handle comma-separated string tags
            self.tags = [tag.strip() for tag in self.tags.split(",")]

        # Author
        self.author = self.metadata.get("author", "Anonymous")

        # Additional metadata
        self.description = self.metadata.get("description", self.excerpt)
        self.image = self.metadata.get("image", "")
        self.featured = self.metadata.get("featured", False)
        self.published = self.metadata.get("published", True)

        # Reading time estimate (words per minute)
        self.reading_time = self._calculate_reading_time()

    def _parse_date(self) -> str:
        """Parse and format the date from various sources."""
        # Try frontmatter date first
        date_value = self.metadata.get("date")
        if date_value:
            try:
                # Handle various date formats
                if isinstance(date_value, datetime):
                    return date_value.strftime("%B %d, %Y")
                elif isinstance(date_value, str):
                    # Try to parse different date formats
                    date_formats = [
                        "%Y-%m-%d",
                        "%d.%m.%Y",
                        "%m/%d/%Y",
                        "%B %d, %Y",
                        "%Y-%m-%d %H:%M:%S",
                    ]
                    for fmt in date_formats:
                        try:
                            parsed_date = datetime.strptime(date_value, fmt)
                            return parsed_date.strftime("%B %d, %Y")
                        except ValueError:
                            continue
            except Exception:
                pass

        # Fallback to file modification time
        try:
            mtime = os.path.getmtime(self.file_path)
            return datetime.fromtimestamp(mtime).strftime("%B %d, %Y")
        except Exception:
            return datetime.now().strftime("%B %d, %Y")

    def _parse_last_modified_date(self) -> str:
        """Parse and format the date from various sources."""
        # Try frontmatter date first
        lm_date_value = self.metadata.get("last_modified")
        if lm_date_value:
            try:
                # Handle various date formats
                if isinstance(lm_date_value, datetime):
                    return lm_date_value.strftime("%B %d, %Y")
                elif isinstance(lm_date_value, str):
                    # Try to parse different date formats
                    date_formats = [
                        "%Y-%m-%d",
                        "%d.%m.%Y",
                        "%m/%d/%Y",
                        "%B %d, %Y",
                        "%Y-%m-%d %H:%M:%S",
                    ]
                    for fmt in date_formats:
                        try:
                            parsed_lm_date = datetime.strptime(lm_date_value, fmt)
                            return parsed_lm_date.strftime("%B %d, %Y")
                        except ValueError:
                            continue
            except Exception:
                pass

        # Fallback to file modification time
        try:
            mtime = os.path.getmtime(self.file_path)
            return datetime.fromtimestamp(mtime).strftime("%B %d, %Y")
        except Exception:
            return datetime.now().strftime("%B %d, %Y")

    def _extract_excerpt(self) -> str:
        """Extract excerpt from frontmatter or content."""
        # Check frontmatter first
        excerpt = self.metadata.get("excerpt")
        if excerpt:
            return excerpt

        # Extract from content
        if not self.content:
            return "Read more..."

        # Remove markdown headers and find first substantial paragraph
        lines = self.content.split("\n")
        for line in lines:
            line = line.strip()
            # Skip empty lines, headers, and code blocks
            if (
                line
                and not line.startswith("#")
                and not line.startswith("```")
                and not line.startswith("---")
                and len(line) > 20
            ):
                # Clean up markdown syntax
                excerpt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)  # Remove links
                excerpt = re.sub(r"[*_`]", "", excerpt)  # Remove emphasis

                if len(excerpt) > 150:
                    excerpt = excerpt[:150] + "..."
                return excerpt

        return "Read more..."

    def _calculate_reading_time(self) -> int:
        """Calculate estimated reading time in minutes."""
        if not self.content:
            return 1

        # Remove markdown syntax for word count
        text = re.sub(r"[#*_`\[\]()]", "", self.content)
        words = len(text.split())

        # Average reading speed: 200 words per minute
        reading_time = max(1, round(words / 200))
        return reading_time

    def to_dict(self) -> Dict:
        """Convert blog post to dictionary for use in Reflex state."""
        return {
            "slug": self.slug,
            "title": self.title,
            "content": self.content,
            "excerpt": self.excerpt,
            "date": self.date,
            "date_published": self.date_published,
            "last_modified": self.last_modified,
            "tags": self.tags,
            "author": self.author,
            "description": self.description,
            "image": self.image,
            "featured": self.featured,
            "published": self.published,
            "reading_time": self.reading_time,
            "file_path": self.file_path,
        }


class BlogParser:
    """Parser for blog posts with frontmatter support."""

    def __init__(self, posts_directory: str):
        self.posts_directory = posts_directory
        self._posts_cache = {}
        self._last_scan_time = 0

    def load_all_posts(self, force_reload: bool = False) -> List[Dict]:
        """Load all blog posts from the directory."""
        # Check if we need to reload (cache invalidation)
        current_time = datetime.now().timestamp()
        if not force_reload and (current_time - self._last_scan_time) < 30:
            # Return cached posts if scanned recently (within 30 seconds)
            if self._posts_cache:
                return list(self._posts_cache.values())

        self._posts_cache = {}
        posts = []

        if not os.path.exists(self.posts_directory):
            print(f"Blog posts directory not found: {self.posts_directory}")
            return []

        # Get all markdown files
        md_files = glob.glob(os.path.join(self.posts_directory, "*.md"))

        for md_file in md_files:
            try:
                blog_post = BlogPost(md_file)

                # Only include published posts
                if blog_post.published:
                    post_dict = blog_post.to_dict()
                    posts.append(post_dict)
                    self._posts_cache[blog_post.slug] = post_dict

            except Exception as e:
                print(f"Error processing blog post {md_file}: {e}")
                continue

        # Sort posts by date (newest first)
        posts.sort(key=lambda x: self._parse_date_for_sorting(x["date"]), reverse=True)

        self._last_scan_time = current_time
        return posts

    def get_post_by_slug(self, slug: str) -> Optional[Dict]:
        """Get a specific post by slug."""
        # Load all posts if not cached
        if not self._posts_cache:
            self.load_all_posts()

        # Try to get from cache first
        post = self._posts_cache.get(slug)
        if post:
            return post

        # If not in cache, try to load the specific file
        md_file = os.path.join(self.posts_directory, f"{slug}.md")
        if os.path.exists(md_file):
            try:
                blog_post = BlogPost(md_file)
                if blog_post.published:
                    post_dict = blog_post.to_dict()
                    self._posts_cache[slug] = post_dict
                    return post_dict
            except Exception as e:
                print(f"Error loading specific post {slug}: {e}")

        return None

    def get_posts_by_tag(self, tag: str) -> List[Dict]:
        """Get all posts with a specific tag."""
        all_posts = self.load_all_posts()
        return [
            post
            for post in all_posts
            if tag.lower() in [t.lower() for t in post["tags"]]
        ]

    def get_featured_posts(self) -> List[Dict]:
        """Get all featured posts."""
        all_posts = self.load_all_posts()
        return [post for post in all_posts if post["featured"]]

    def get_recent_posts(self, limit: int = 5) -> List[Dict]:
        """Get recent posts (already sorted by date)."""
        all_posts = self.load_all_posts()
        return all_posts[:limit]

    def _parse_date_for_sorting(self, date_str: str) -> datetime:
        """Parse date string for sorting purposes."""
        try:
            return datetime.strptime(date_str, "%B %d, %Y")
        except ValueError:
            # Fallback to current date if parsing fails
            return datetime.now()

    def get_all_tags(self) -> List[str]:
        """Get all unique tags from all posts."""
        all_posts = self.load_all_posts()
        tags = set()
        for post in all_posts:
            tags.update(post["tags"])
        return sorted(list(tags))


# Global instance for the application
BLOG_POSTS_DIR = "/home/alex/retest/retest/public/blog_posts"
blog_parser = BlogParser(BLOG_POSTS_DIR)
