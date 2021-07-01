import pytest

#read module three pdf to finish 
@patch('requests.get')
def test_can_create_item(mock_get,example_fixture):
    assert example_fixture == "some text "  

@pytest.fixture
def example_fixture():
    return "some text "