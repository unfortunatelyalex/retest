import reflex as rx
import os
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="retest",
    frontend_port=os.getenv("REFLEX_FRONTEND_PORT"),
    backend_port=os.getenv("REFLEX_BACKEND_PORT"),
    loglevel=os.getenv("REFLEX_LOGLEVEL"),
    deploy_url="https://retest.alexdot.me",
    show_built_with_reflex=False,
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.SitemapPlugin()],
)
