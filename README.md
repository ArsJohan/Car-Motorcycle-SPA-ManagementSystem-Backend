# BACKEND-SYSTEM-AUTO-AND-MOTORCYCLE-SPA

A backend system built with Python and FastAPI to manage clients, vehicles, services, discounts, and payments for an auto and motorcycle spa. Implements clean architecture principles, RESTful APIs, role-based authentication, and database migrations with SQLAlchemy + Alembic. Includes Docker Compose and Pytest for automated testing.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Clean Architecture**: Organized in layers (API, Services, Repositories, Models)
- **Database Management**: SQLAlchemy ORM with Alembic migrations
- **PostgreSQL**: Robust database for production use
- **Docker Support**: Complete Docker Compose setup
- **Testing**: Comprehensive test suite with Pytest
- **Health Monitoring**: Built-in health check endpoints

## 📁 Project Structure

```
├── api/                    # API layer - endpoints and routers
├── services/               # Business logic layer
├── repositories/           # Data access layer
├── models/                 # Database models
├── core/                   # Core configuration and database setup
├── tests/                  # Test suite
├── alembic/                # Database migration files
├── docker-compose.yml      # Docker services configuration
├── Dockerfile             # Container build instructions
├── pyproject.toml         # Project dependencies and configuration
├── requirements.txt       # Python dependencies
├── alembic.ini            # Alembic configuration
├── start.sh               # Startup script
└── README.md              # This file
```

## 🛠️ Setup and Installation

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (for containerized deployment)
- PostgreSQL (if running locally without Docker)

### Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArsJohan/BACKEND-SYSTEM-AUTO-AND-MOTORCYCLE-SPA.git
   cd BACKEND-SYSTEM-AUTO-AND-MOTORCYCLE-SPA
   ```

2. **Start services with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - API: http://localhost:8000
   - Health Check: http://localhost:8000/health
   - API Documentation: http://localhost:8000/docs

### Local Development Setup

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # OR using pyproject.toml
   pip install -e ".[dev]"
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your database configuration
   ```

4. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   ./start.sh
   # OR manually:
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_main.py
```

## 📋 API Endpoints

### Health Check
- `GET /health` - Application health status
- `GET /` - Root endpoint with application info

### API Documentation
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## 🗄️ Database Management

### Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migrations:
```bash
alembic downgrade -1  # Rollback one migration
```

## 🐳 Docker Commands

```bash
# Build and start services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Rebuild services
docker-compose up -d --build
```

## 🛡️ Environment Variables

Key environment variables (see `.env.example`):

- `APP_NAME`: Application name
- `DEBUG`: Enable/disable debug mode
- `DATABASE_URL`: Complete database connection string
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `POSTGRES_HOST`: Database host
- `POSTGRES_PORT`: Database port

## 🏗️ Architecture

This project follows Clean Architecture principles:

1. **API Layer** (`api/`): HTTP endpoints and request/response handling
2. **Service Layer** (`services/`): Business logic and orchestration
3. **Repository Layer** (`repositories/`): Data access and persistence
4. **Model Layer** (`models/`): Database models and schemas
5. **Core** (`core/`): Configuration, database setup, and utilities

## 📝 Development Guidelines

- Follow PEP 8 style guide
- Write comprehensive tests for new features
- Use type hints for better code documentation
- Follow the repository pattern for data access
- Keep business logic in services
- Use dependency injection for better testability

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Johan Esteban Arias Arboleda**

---

🚗 Built with ❤️ for the auto and motorcycle spa industry
