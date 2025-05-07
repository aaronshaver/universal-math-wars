import pytest
from sqlmodel import Session
from sqlalchemy.exc import ResourceClosedError

from database import get_session, engine # Assuming User and other models might be needed later if tests expand


def test_get_session():
    """
    Tests that get_session() correctly yields a database session
    and that the session is closed after use.
    """
    session_generator = get_session()
    db_session = next(session_generator)

    assert db_session is not None
    assert isinstance(db_session, Session)
    assert db_session.is_active

    # Check that the session is closed after the generator is exhausted
    with pytest.raises(StopIteration):
        next(session_generator) # Exhaust the generator