"""
Amenity related functionality
"""

from datetime import datetime
from typing import Any, Optional
from sqlalchemy import Column, String, ForeignKey, DateTime
from src.models.base import BaseModel
from src.persistence import repo

class Amenity(BaseModel):
    """Amenity representation"""

    __tablename__ = 'amenity'

    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, name: str, **kw) -> None:
        """Init method with necessary attributes"""
        super().__init__(**kw)
        self.name = name

    def __repr__(self) -> str:
        """Represent the amenity object as a string"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        amenity = Amenity(**data)
        repo.save(amenity)
        return amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity | None":
        """Update an existing amenity"""
        amenity: Amenity | None = Amenity.get(amenity_id)

        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]

        repo.update(amenity)
        return amenity


class PlaceAmenity(BaseModel):
    """PlaceAmenity representation"""

    __tablename__ = 'place_amenity'

    place_id = db.Column(db.String(36), ForeignKey('place.id'), nullable=False)
    amenity_id = db.Column(db.String(36), ForeignKey('amenity.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, place_id: str, amenity_id: str, **kw) -> None:
        """Init method with necessary attributes"""
        super().__init__(**kw)
        self.place_id = place_id
        self.amenity_id = amenity_id

    def __repr__(self) -> str:
        """Represent the PlaceAmenity object as a string"""
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
      return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def get(place_id: str, amenity_id: str) -> "PlaceAmenity | None":
        """Get a PlaceAmenity object by place_id and amenity_id"""
        place_amenity: PlaceAmenity | None = (
            repo.get_all("placeamenity")
            .filter_by(place_id=place_id, amenity_id=amenity_id)
            .first()
        )
        return place_amenity

    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Create a new PlaceAmenity object"""
        new_place_amenity = PlaceAmenity(**data)
        repo.save(new_place_amenity)
        return new_place_amenity

    @staticmethod
    def delete(place_id: str, amenity_id: str) -> bool:
        """Delete a PlaceAmenity object by place_id and amenity_id"""
        place_amenity = PlaceAmenity.get(place_id, amenity_id)
        if not place_amenity:
            return False

        repo.delete(place_amenity)
        return True