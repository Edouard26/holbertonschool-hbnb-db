"""
Place related functionality
"""

from datetime import datetime
from typing import Any, Optional
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import BaseModel
from src.models.city import City
from src.models.user import User
from src.persistence import repo


class Place(BaseModel):
    """Place representation"""

    __tablename__ = 'place'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), ForeignKey('user.id'), nullable=False)
    city_id = db.Column(db.String(36), ForeignKey('city.id'), nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, data: dict | None = None, **kw) -> None:
        """Init method with necessary attributes"""
        super().__init__(**kw)
        if not data:
            return
        self.name = data.get("name", "")
        self.description = data.get("description", "")
        self.address = data.get("address", "")
        self.latitude = float(data.get("latitude", 0.0))
        self.longitude = float(data.get("longitude", 0.0))
        self.host_id = data["host_id"]
        self.city_id = data["city_id"]
        self.price_per_night = int(data.get("price_per_night", 0))
        self.number_of_rooms = int(data.get("number_of_rooms", 0))
        self.number_of_bathrooms = int(data.get("number_of_bathrooms", 0))
        self.max_guests = int(data.get("max_guests", 0))

    def __repr__(self) -> str:
        """Represent the place object as a string"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "Place":
        """Create a new place"""
        user: User | None = User.get(data["host_id"])
        if not user:
            raise ValueError(f"User with ID {data['host_id']} not found")

        city: City | None = City.get(data["city_id"])
        if not city:
            raise ValueError(f"City with ID {data['city_id']} not found")

        new_place = Place(data=data)
        repo.save(new_place)
        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> "Place | None":
        """Update an existing place"""
        place: Place | None = Place.get(place_id)

        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        place.updated_at = datetime.utcnow()
        repo.update(place)

        return place