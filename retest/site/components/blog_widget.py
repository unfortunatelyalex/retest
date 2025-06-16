# site/components/blog_widget.py
import reflex as rx
import os
import glob
from typing import List, Dict


class BlogState(rx.State):
    """State for managing blog posts from markdown files."""
    posts: List[Dict] = []

    @rx.event
    def load_posts(self):
        """Load all blog posts from markdown files."""
        posts_dir = "/home/ubuntu/retest/retest/public/blog_posts"
        self.posts = []

        if os.path.exists(posts_dir):
            md_files = glob.glob(os.path.join(posts_dir, "*.md"))
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Extract filename for slug
                    filename = os.path.basename(md_file)
                    slug = os.path.splitext(filename)[0]

                    # Parse frontmatter and content
                    lines = content.split('\n')
                    title = slug.replace('-', ' ').replace('_', ' ').title()
                    excerpt = "Read more..."

                    # Try to extract title from first heading
                    for line in lines:
                        if line.startswith('# '):
                            title = line[2:].strip()
                            break

                    # Extract excerpt from first paragraph
                    for line in lines:
                        if line.strip() and not line.startswith('#') and not line.startswith('---'):
                            excerpt = line.strip()
                            if len(excerpt) > 100:
                                excerpt = excerpt[:100] + "..."
                            break

                    post = {
                        "slug": slug,
                        "title": title,
                        "excerpt": excerpt,
                        "content": content,
                        "date": "Recent",  # Could be extracted from file date
                        "tags": ["Blog"]
                    }
                    self.posts.append(post)
                except Exception as e:
                    print(f"Error loading {md_file}: {e}")

        # Sort posts by filename for consistent ordering
        self.posts.sort(key=lambda x: x['slug'])

    @rx.var
    def preview_posts(self) -> List[Dict]:
        """Get only the first 3 posts for preview."""
        return self.posts[:3]

    @rx.var
    def has_more_posts(self) -> bool:
        """Check if there are more than 3 posts."""
        return len(self.posts) > 3

    @rx.var
    def posts_count(self) -> int:
        """Get the total number of posts."""
        return len(self.posts)

    def get_post_by_slug(self, slug: str) -> Dict | None:
        """Get a specific post by slug."""
        for post in self.loaded_posts:
            if post['slug'] == slug:
                return post
        return None


# Keep the old POSTS for backward compatibility, but make it dynamic
POSTS = [
    {
        "slug": "hello-world",
        "title": "Hello World",
        "date": "June 10, 2025",
        "excerpt": "My first blog post about getting started with Reflex and web development.",
        "tags": ["Intro", "Reflex"],
        "body": "# Hello World\n\nWelcome to my blog!"
    },
    {
        "slug": "reflex-tips",
        "title": "Building Apps with Reflex",
        "date": "May 5, 2025",
        "excerpt": "Essential tips and tricks for building modern web applications with Reflex.",
        "tags": ["Tutorial", "Reflex"],
        "body": "# Building Apps with Reflex\n\nHere are some great tips for building with Reflex..."
    },
]


def BlogPreviewWidget():
    return rx.vstack(
        rx.hstack(
            rx.heading("📜 Latest Posts", size="3",
                       margin_bottom="0.25em"),  # Smaller heading
            rx.spacer(),
            rx.link(
                rx.icon_button(
                    rx.icon("external-link", size=14),  # Smaller icon
                    variant="ghost",
                    size="2",  # Smaller button
                    aria_label="View all posts"
                ),
                href="/blog"
            ),
            align_items="center",
            width="100%"
        ),
        rx.vstack(
            rx.foreach(
                BlogState.preview_posts,
                lambda post: rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.link(
                                post["title"],
                                href=f"/blog/{post['slug']}",
                                weight="medium",
                                color_scheme="blue",
                                style={
                                    "_hover": {"text_decoration": "underline"}
                                }
                            ),
                            rx.spacer(),
                            rx.text(
                                post.get("date", ""),
                                size="1",
                                color_scheme="gray"
                            ),
                            align_items="center",
                            width="100%"
                        ),
                        rx.text(
                            post.get("excerpt", ""),
                            size="2",
                            color_scheme="gray",
                            line_height="1.4"
                        ),
                        rx.text(
                            "Tags: Blog",
                            size="1",
                            color_scheme="gray"
                        ),
                        align_items="start",
                        spacing="1",  # Reduced spacing
                        padding="0.5rem",  # Reduced padding
                        border_radius="md",
                        style={
                                "_hover": {
                                    "background_color": rx.color("gray", 2),
                                    "transition": "background-color 0.2s ease"
                                }
                        }
                    ),
                    width="100%"
                )
            ),
            rx.cond(
                BlogState.preview_posts.length() == 0,
                rx.text("No blog posts available.",
                        size="2", color_scheme="gray"),
                rx.fragment()
            ),
            spacing="2",
            width="100%"
        ),
        rx.cond(
            BlogState.has_more_posts,
            rx.link(
                rx.hstack(
                    rx.text("View all posts", size="2"),
                    rx.icon("arrow-right", size=14),
                    align_items="center",
                    spacing="1"
                ),
                href="/blog",
                color_scheme="blue",
                margin_top="0.5rem"
            ),
            rx.cond(
                BlogState.preview_posts.length() > 0,
                rx.text(f"All {BlogState.preview_posts.length()} posts shown",
                        size="1", color_scheme="gray", margin_top="0.5rem"),
                rx.fragment()
            )
        ),
        align_items="start",
        spacing="2",  # Reduced spacing
        padding="1rem",  # Added explicit padding
        width="100%",
        height="auto",  # Let content determine height
        on_mount=BlogState.load_posts  # Load posts when widget mounts
    )
