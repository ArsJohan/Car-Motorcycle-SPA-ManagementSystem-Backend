#!/bin/bash

# Auto and Motorcycle Spa Backend Startup Script

echo "🚗 Starting Auto and Motorcycle Spa Backend..."

# Check if .env file exists, if not copy from example
if [ ! -f .env ]; then
    echo "📋 Creating .env file from .env.example..."
    cp .env.example .env
fi

# Install dependencies if requirements.txt exists
if [ -f requirements.txt ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Run database migrations (if Alembic is available)
if command -v alembic &> /dev/null; then
    echo "🗄️ Running database migrations..."
    alembic upgrade head
fi

# Start the application
echo "🚀 Starting the FastAPI application..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload