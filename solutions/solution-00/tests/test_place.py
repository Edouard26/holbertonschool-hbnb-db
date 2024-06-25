from src.models.place import Place

def test_create_place(session):
    place_data = {
        "name": "Cozy Cottage",
        "description": "A cozy and warm cottage in the woods.",
        "address": "123 Forest Lane",
        "latitude": 45.0,
        "longitude": -75.0,
        "host_id": "1",
        "city_id": "1",
        "price_per_night": 100,
        "number_of_rooms": 2,
        "number_of_bathrooms": 1,
        "max_guests": 4
    }
    place = Place.create(place_data)
    session.add(place)
    session.commit()

    fetched_place = session.query(Place).filter_by(name="Cozy Cottage").first()
    assert fetched_place is not None
    assert fetched_place.address == "123 Forest Lane"

def test_update_place(session):
    place = session.query(Place).filter_by(name="Cozy Cottage").first()
    Place.update(place.id, {"description": "Updated description"})
    session.commit()

    updated_place = session.query(Place).filter_by(name="Cozy Cottage").first()
    assert updated_place.description == "Updated description"

def test_delete_place(session):
    place = session.query(Place).filter_by(name="Cozy Cottage").first()
    session.delete(place)
    session.commit()

    deleted_place = session.query(Place).filter_by(name="Cozy Cottage").first()
    assert deleted_place is None