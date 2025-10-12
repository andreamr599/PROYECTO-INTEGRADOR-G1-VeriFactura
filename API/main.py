from __future__ import annotations

import logging

from fastapi import FastAPI
import uvicorn

from app import create_app
from app.config import Config

logging.basicConfig(level=logging.INFO)

def _initialise_app() -> FastAPI:
    config = Config()
    app = create_app(config)
    return app


app = _initialise_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
