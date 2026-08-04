import os

from fastapi.staticfiles import StaticFiles

from .api import app

frontend_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)

app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
