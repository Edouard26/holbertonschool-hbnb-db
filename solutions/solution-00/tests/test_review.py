from src.models.review import Review
from src.models.place import Place
from src.models.user import User
from src.models.city import City

def test_create_review(session):
    # Ensure necessary related records exist
    user_data = {"email": "reviewer@example.com", "first_name": "Reviewer", "last_name": "User", "password": "password123", "is_admin": False}
    user = User.create(user_data)
    session.add(user)
    
    city_data = {"name": "Review City", "country_code": "RC"}
    city = City.create(city_data)
    session.add(city)
    
    place_data = {
        "name": "Review Cottage",
        "description": "A cozy and warm place.",
        "address": "456 Review Lane",
        "latitude": 50.0,
        "longitude": -80.0,
        "host_id": user.id,  # Use the created user ID
        "city_id": city.id,  # Use the created city ID
        "price_per_night": 150,
        "number_of_rooms": 3,
        "number_of_bathrooms": 2,
        "max_guests": 5
    }
    place = Place.create(place_data)
    session.add(place)
    session.commit()

    review_data = {
        "place_id": place.id,
        "user_id": user.id,
        "comment": "Great place!",
        "rating": 4.5
    }
    review = Review.create(review_data)
    session.add(review)
    session.commit()

    fetched_review = session.query(Review).filter_by(comment="Great place!").first()
    assert fetched_review is not None
    assert fetched_review.rating == 4.5

def test_update_review(session):
    review = session.query(Review).filter_by(comment="Great place!").first()
    Review.update(review.id, {"comment": "Amazing place!"})
    session.commit()

    updated_review = session.query(Review).filter_by(comment="Amazing place!").first()
    assert updated_review is not None
    assert updated_review.comment == "Amazing place!"

def test_delete_review(session):
    review = session.query(Review).filter_by(comment="Amazing place!").first()
    session.delete(review)
    session.commit()

    deleted_review = session.query(Review).filter_by(comment="Amazing place!").first()
    assert deleted_review is None