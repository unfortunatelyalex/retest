"""Portfolio website built with Reflex."""

import reflex as rx
from .pages import (
    about_page,
    projects_page,
    skills_page,
    blog_page,
    contact_page,
)
from .pages.blog_post import blog_post_page

# Set app styles
app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        radius="medium",
        scaling="100%",
    ),
)

# Add pages to the app
app.add_page(about_page, route="/", title="About - Alex Portfolio")
app.add_page(projects_page, route="/projects", title="Projects - Alex Portfolio")
app.add_page(skills_page, route="/skills", title="Skills - Alex Portfolio")
app.add_page(blog_page, route="/blog", title="Blog - Alex Portfolio")
app.add_page(blog_post_page, route="/blog/[post_id]", title="Blog Post - Alex Portfolio")
app.add_page(contact_page, route="/contact", title="Contact - Alex Portfolio")
