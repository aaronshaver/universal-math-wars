import os

def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest file
    after command line options have been parsed.
    """
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_USER"] = "dev_user"
    os.environ["DB_PASSWORD"] = "dev_password"
    os.environ["DB_NAME"] = "mathwars_db" 