from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="IA Team Platform",
    version="1.0.0",
)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
