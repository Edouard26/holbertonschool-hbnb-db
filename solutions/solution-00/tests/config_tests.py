import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import SQLAlchemyBase

DATABASE_URL = "sqlite:///test.db"

@pytest.fixture(scope='module')
def test_engine():
    """Create a new database engine for tests."""
    return create_engine(DATABASE_URL)

@pytest.fixture(scope='module')
def tables(test_engine):
    """Create database tables."""
    SQLAlchemyBase.metadata.create_all(test_engine)
    yield
    SQLAlchemyBase.metadata.drop_all(test_engine)

@pytest.fixture
def session(test_engine, tables):
    """Create a new database session for tests."""
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()