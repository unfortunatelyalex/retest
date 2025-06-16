import reflex as rx

config = rx.Config(
    app_name="retest",
    frontend_port=1234,
    backend_port=5678,
    backend_host="0.0.0.0",  # Allow connections from any host
    plugins=[rx.plugins.TailwindV4Plugin()]
)