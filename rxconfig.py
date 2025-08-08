import reflex as rx
import os
from dotenv import load_dotenv

load_dotenv()


def _to_int(val: str | None, default: int) -> int:
    try:
        return int(val) if val is not None else default
    except ValueError:
        return default


config = rx.Config(
    app_name="retest",
    frontend_port=_to_int(os.getenv("REFLEX_FRONTEND_PORT"), 3000),
    backend_port=_to_int(os.getenv("REFLEX_BACKEND_PORT"), 8000),
    # Keep default log level if env not supported in this version
    deploy_url=os.getenv("REFLEX_DEPLOY_URL") or "",
    show_built_with_reflex=False,
    plugins=[rx.plugins.TailwindV4Plugin(), rx.plugins.sitemap.SitemapPlugin()],
)
