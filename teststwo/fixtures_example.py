import pytest

@pytest.fixture
def sample_data():
    # Setup: Creating data or state needed for the test
    data = {"name": "John", "age": 30}
    yield data  # Test function will get this value
    # Teardown: Any necessary cleanup after the test runs
    print("Teardown after test")

@pytest.fixture(scope="module")
def db_connection():
    connection = connect_to_db()
    yield connections
    connection.close()  # Teardown

def test_sample(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30



