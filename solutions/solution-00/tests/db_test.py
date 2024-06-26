import pytest
from app import app, db

@pytest.fixture
def app_context():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

def test_database_connection(app_context):

    user = User(username='test_user')
    db.session.add(user)
    db.session.commit()

    assert User.query.filter_by(username='test_user').first() is not None