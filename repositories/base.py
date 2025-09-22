from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository(Generic[T], ABC):
    """Base repository interface."""
    
    def __init__(self, db: Session, model_class):
        self.db = db
        self.model_class = model_class
    
    def get_all(self) -> List[T]:
        """Get all records."""
        return self.db.query(self.model_class).all()
    
    def get_by_id(self, id: int) -> Optional[T]:
        """Get a record by ID."""
        return self.db.query(self.model_class).filter(self.model_class.id == id).first()
    
    def create(self, obj_in: dict) -> T:
        """Create a new record."""
        obj = self.model_class(**obj_in)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, id: int, obj_in: dict) -> Optional[T]:
        """Update a record."""
        obj = self.get_by_id(id)
        if obj:
            for field, value in obj_in.items():
                setattr(obj, field, value)
            self.db.commit()
            self.db.refresh(obj)
        return obj
    
    def delete(self, id: int) -> bool:
        """Delete a record."""
        obj = self.get_by_id(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
            return True
        return False