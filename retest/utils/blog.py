"""Blog utilities for reading and parsing markdown blog posts."""
import frontmatter
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path


def get_blog_posts_directory() -> Path:
    """Get the blog posts directory path."""
    # Get the current file's directory (utils)
    current_dir = Path(__file__).parent
    # Go up to retest directory, then to public/blog_posts
    blog_dir = current_dir.parent / "public" / "blog_posts"
    return blog_dir


def parse_blog_post(file_path: Path) -> Optional[Dict]:
    """Parse a single blog post markdown file with frontmatter.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        Dictionary with blog post data or None if parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Extract filename without extension for ID
        post_id = file_path.stem
        
        # Parse metadata
        metadata = post.metadata
        
        # Calculate read time (rough estimate: 200 words per minute)
        word_count = len(post.content.split())
        read_time = max(1, round(word_count / 200))
        
        return {
            "id": post_id,
            "title": metadata.get("title", "Untitled"),
            "excerpt": metadata.get("excerpt", ""),
            "description": metadata.get("description", ""),
            "date": metadata.get("date", ""),
            "last_modified": metadata.get("last_modified", ""),
            "author": metadata.get("author", "Anonymous"),
            "tags": metadata.get("tags", []),
            "featured": metadata.get("featured", False),
            "published": metadata.get("published", True),
            "read_time": f"{read_time} min read",
            "content": post.content,
            "word_count": word_count
        }
    except Exception as e:
        print(f"Error parsing blog post {file_path}: {e}")
        return None


def load_all_blog_posts() -> List[Dict]:
    """Load and parse all blog posts from the blog_posts directory.
    
    Returns:
        List of blog post dictionaries, sorted by date (newest first)
    """
    blog_posts = []
    blog_dir = get_blog_posts_directory()
    
    if not blog_dir.exists():
        print(f"Blog directory not found: {blog_dir}")
        return []
    
    # Find all markdown files
    markdown_files = list(blog_dir.glob("*.md"))
    
    for file_path in markdown_files:
        post_data = parse_blog_post(file_path)
        if post_data and post_data.get("published", True):
            blog_posts.append(post_data)
    
    # Sort by date (newest first) - handle various date formats
    def parse_date(date_str: str) -> datetime:
        """Parse date string in various formats."""
        if not date_str:
            return datetime.min
        
        # Try different date formats
        formats = [
            "%d.%m.%Y",      # DD.MM.YYYY
            "%Y-%m-%d",      # YYYY-MM-DD
            "%m/%d/%Y",      # MM/DD/YYYY
            "%d/%m/%Y",      # DD/MM/YYYY
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        # If no format works, return minimum date
        print(f"Could not parse date: {date_str}")
        return datetime.min
    
    blog_posts.sort(key=lambda x: parse_date(x.get("date", "")), reverse=True)
    
    return blog_posts


def get_featured_blog_posts() -> List[Dict]:
    """Get only featured blog posts.
    
    Returns:
        List of featured blog post dictionaries
    """
    all_posts = load_all_blog_posts()
    return [post for post in all_posts if post.get("featured", False)]


def get_blog_post_by_id(post_id: str) -> Optional[Dict]:
    """Get a specific blog post by its ID.
    
    Args:
        post_id: The blog post ID (filename without extension)
        
    Returns:
        Blog post dictionary or None if not found
    """
    blog_dir = get_blog_posts_directory()
    file_path = blog_dir / f"{post_id}.md"
    
    if file_path.exists():
        return parse_blog_post(file_path)
    
    return None


def get_blog_tags() -> List[str]:
    """Get all unique tags from all blog posts.
    
    Returns:
        Sorted list of unique tags
    """
    all_posts = load_all_blog_posts()
    tags = set()
    
    for post in all_posts:
        tags.update(post.get("tags", []))
    
    return sorted(list(tags))
