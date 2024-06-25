from src.models.city import City
from src.models.country import Country

def test_create_city(session):
    # Ensure necessary related records exist
    country_data = {"name": "Test Country", "code": "TC"}
    country = Country.create(country_data)
    session.add(country)
    session.commit()

    city_data = {
        "name": "Test City",
        "country_code": country.code  # Use the created country code
    }
    city = City.create(city_data)
    session.add(city)
    session.commit()

    fetched_city = session.query(City).filter_by(name="Test City").first()
    assert fetched_city is not None
    assert fetched_city.name == "Test City"

def test_update_city(session):
    city = session.query(City).filter_by(name="Test City").first()
    City.update(city.id, {"name": "Updated City"})
    session.commit()

    updated_city = session.query(City).filter_by(name="Updated City").first()
    assert updated_city.name == "Updated City"

def test_delete_city(session):
    city = session.query(City).filter_by(name="Updated City").first()
    session.delete(city)
    session.commit()

    deleted_city = session.query(City).filter_by(name="Updated City").first()
    assert deleted_city is None