"""
City related functionality
"""

from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from src.models.base import BaseModel
from src.models.country import Country
from src.persistence import repo

class City(BaseModel):
    """City representation"""

    __tablename__ = 'city'

    name = db.Column(db.String(255), nullable=False)
    country_code = db.Column(db.String(36), ForeignKey('country.code'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Init method with necessary attributes"""
        super().__init__(**kw)
        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        """Represent the city object as a string"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        country = Country.get(data["country_code"])
        if not country:
            raise ValueError("Country not found")
        
        city = City(**data)
        repo.save(city)
        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """Update an existing city"""
        city = City.get(city_id)
        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        city.updated_at = datetime.utcnow()
        repo.update(city)
        return city