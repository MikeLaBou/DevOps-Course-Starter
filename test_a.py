import pytest

def test_can_create_item(example_fixture):
    assert example_fixture == "some text "  

@pytest.fixture
def example_fixture():
    return "some text "