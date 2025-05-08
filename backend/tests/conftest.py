import os
import pytest

# TEST_DB_NAME = "mathwars_test_db" # No longer needed for mocking

# The manage_test_database fixture is no longer needed for mocking approach.

def pytest_configure(config):
    """
    Minimal configuration for tests. 
    DB environment variables might still be set here if other tests 
    (not using mocks) were to be added later and needed them for a real DB.
    For pure mock-based tests, these might not be strictly necessary immediately,
    but keeping them doesn't harm and aligns with original intent if you mix strategies later.
    """
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_USER"] = "dev_user"
    os.environ["DB_PASSWORD"] = "dev_password"
    # os.environ["DB_NAME"] = TEST_DB_NAME # Not setting to TEST_DB_NAME as engine isn't used by mock tests
    # Setting a placeholder or the actual main DB name might be relevant if some parts of app
    # still try to initialize based on it, though for mocked sessions it won't connect.
    os.environ["DB_NAME"] = "mathwars_db" # Or any placeholder if your app needs it defined.