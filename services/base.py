from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class BaseService(Generic[T], ABC):
    """Base service interface."""
    
    def __init__(self, repository):
        self.repository = repository
    
    def get_all(self):
        """Get all items."""
        return self.repository.get_all()
    
    def get_by_id(self, id: int):
        """Get item by ID."""
        return self.repository.get_by_id(id)
    
    def create(self, obj_in: dict):
        """Create a new item."""
        return self.repository.create(obj_in)
    
    def update(self, id: int, obj_in: dict):
        """Update an item."""
        return self.repository.update(id, obj_in)
    
    def delete(self, id: int):
        """Delete an item."""
        return self.repository.delete(id)