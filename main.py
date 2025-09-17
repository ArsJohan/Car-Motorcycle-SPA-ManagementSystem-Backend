from fastapi import FastAPI
from core.config import settings

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    description="A backend system to manage clients, vehicles, services, discounts, and payments for an auto and motorcycle spa",
    version="0.1.0",
    debug=settings.debug,
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": "0.1.0"
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": "0.1.0",
        "health_check": "/health"
    }