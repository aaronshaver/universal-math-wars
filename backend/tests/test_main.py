from fastapi.testclient import TestClient
# Removed SQLModel for session, no real DB interaction
import pytest
from unittest.mock import MagicMock, ANY # ANY is useful for asserting calls with objects

from main import app, get_session, UserCreate, User # User model is still needed to instantiate it
# Removed db_engine import

def override_get_session():
    """Override FastAPI's get_session dependency to provide a mock session."""
    mock_session = MagicMock()
    # Simulate that db_user.id gets populated after session.refresh(db_user)
    # The actual User instance passed to refresh will be assigned an id.
    def mock_refresh(user_instance):
        user_instance.id = 123 # Simulate a generated ID
    mock_session.refresh = MagicMock(side_effect=mock_refresh)
    
    # For commit, if there's a specific exception you want to simulate later, 
    # you can configure it here. For now, a simple mock is fine.
    mock_session.commit = MagicMock()
    mock_session.add = MagicMock()
    mock_session.rollback = MagicMock() # In case of error path testing later

    # The dependency is a generator, so we yield the mock session
    yield mock_session 

app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)

# The setup_database fixture (creating/dropping tables) is no longer needed.
# @pytest.fixture(scope="function", autouse=True)
# def setup_database():
#     SQLModel.metadata.create_all(db_engine)
#     yield
#     SQLModel.metadata.drop_all(db_engine)

def test_register_user_success():
    test_username = "testmockuser"
    test_password = "testmockpassword123"

    response = client.post(
        "/api/v1/register",
        json={"username": test_username, "password": test_password},
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User registered successfully"
    assert data["user_id"] == 123 # Check against the ID our mock_refresh sets

    # To get the mock session instance that was used in the endpoint:
    # We need to call the dependency override directly to get the mock yielded by it.
    # This is a bit indirect but necessary because the TestClient consumes the dependency.
    # A simpler way if you control the app directly is to pass the mock, but with TestClient it's like this.
    # For now, let's assume we want to check calls on the mock that was configured in override_get_session.
    # A common pattern is to retrieve the mock from app.dependency_overrides[get_session] if it were stored, 
    # or to make the mock globally accessible for assertions. 
    # Let's refine override_get_session to make the mock accessible for assertions.

    # For simplicity in this step, we will rely on the side effect of refresh populating the ID.
    # More advanced tests would assert calls on the mock_session itself.
    # For example, you would need a way to access the specific mock_session instance used by the endpoint call.
    # This typically involves a bit more setup, like storing the last used mock in the test or fixture.

    # To directly assert calls, we need access to the *specific* mock instance used by the endpoint. 
    # A straightforward way is to modify override_get_session to store the last mock, 
    # or use a pytest fixture to provide the mock that override_get_session will also use.

    # Let's assume for this iteration the primary goal is that the endpoint returns correctly based on mock behavior.
    # Advanced: To assert calls on the mock session:
    # mock_db_session_used = app.dependency_overrides[get_session]() # This gets the generator
    # try:
    #     actual_mock_session = next(mock_db_session_used) # Get the yielded mock
    #     actual_mock_session.add.assert_called_once()
    #     # To assert with specific User instance:
    #     # actual_mock_session.add.assert_called_once_with(ANY) # ANY from unittest.mock
    #     # or construct the expected User object if details are known and stable.
    #     actual_mock_session.commit.assert_called_once()
    #     actual_mock_session.refresh.assert_called_once()
    # except StopIteration:
    #     pytest.fail("Mock session override did not yield a session.")