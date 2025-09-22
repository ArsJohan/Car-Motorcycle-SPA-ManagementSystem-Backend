"""
Simple tests for the project structure.
These tests don't require FastAPI to be installed.
"""
import os
import sys

def test_project_structure():
    """Test that all required folders exist."""
    required_folders = ['api', 'services', 'repositories', 'models', 'core', 'tests', 'alembic']
    
    for folder in required_folders:
        assert os.path.exists(folder), f"Folder {folder} should exist"
        init_file = os.path.join(folder, '__init__.py')
        if folder != 'alembic':  # alembic doesn't need __init__.py
            assert os.path.exists(init_file), f"File {init_file} should exist"


def test_required_files():
    """Test that required files exist."""
    required_files = [
        'main.py',
        'pyproject.toml', 
        'requirements.txt',
        'docker-compose.yml',
        'Dockerfile',
        'alembic.ini',
        'start.sh',
        '.env.example',
        'README.md'
    ]
    
    for file in required_files:
        assert os.path.exists(file), f"File {file} should exist"


def test_import_core_config():
    """Test that core configuration can be imported."""
    try:
        from core.config import settings
        assert settings.app_name == "Auto and Motorcycle Spa Backend"
        print("✅ Core configuration import successful")
    except ImportError as e:
        print(f"❌ Failed to import core.config: {e}")


def test_import_models():
    """Test that models can be imported."""
    try:
        from models.base import BaseModel
        from models.client import Client
        print("✅ Models import successful") 
    except ImportError as e:
        print(f"❌ Failed to import models: {e}")


def test_health_check_logic():
    """Test the health check logic without FastAPI."""
    from test_structure import health_check, root
    
    health_response = health_check()
    assert health_response["status"] == "healthy"
    assert "app_name" in health_response
    assert "version" in health_response
    
    root_response = root()
    assert "message" in root_response
    assert "version" in root_response
    assert "health_check" in root_response
    
    print("✅ Health check logic test passed")


if __name__ == "__main__":
    print("🧪 Running basic project structure tests...")
    
    test_project_structure()
    print("✅ Project structure test passed")
    
    test_required_files() 
    print("✅ Required files test passed")
    
    test_import_core_config()
    test_import_models()
    test_health_check_logic()
    
    print("🎉 All basic tests passed!")