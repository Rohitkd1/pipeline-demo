import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_users_returns_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_single_user_has_required_fields():
    response = requests.get(f"{BASE_URL}/users/1")
    user = response.json()
    assert "id" in user
    assert "name" in user
    assert "email" in user