from src.models.amenity import Amenity

def test_create_amenity(session):
    amenity_data = {
        "name": "Swimming Pool"
    }
    amenity = Amenity.create(amenity_data)
    session.add(amenity)
    session.commit()

    fetched_amenity = session.query(Amenity).filter_by(name="Swimming Pool").first()
    assert fetched_amenity is not None
    assert fetched_amenity.name == "Swimming Pool"

def test_update_amenity(session):
    amenity = session.query(Amenity).filter_by(name="Swimming Pool").first()
    Amenity.update(amenity.id, {"name": "Heated Pool"})
    session.commit()

    updated_amenity = session.query(Amenity).filter_by(name="Heated Pool").first()
    assert updated_amenity is not None
    assert updated_amenity.name == "Heated Pool"

def test_delete_amenity(session):
    amenity = session.query(Amenity).filter_by(name="Heated Pool").first()
    session.delete(amenity)
    session.commit()

    deleted_amenity = session.query(Amenity).filter_by(name="Heated Pool").first()
    assert deleted_amenity is None