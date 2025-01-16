from services.booker_service import BookerService


def test_booker_auth():
    booker = BookerService()
    response = booker.auth("admin", "password123")

    assert response["token"]


def test_create_add_get(base_url):
    response = requests.get(base_url + "/update/add")
    assert response.status_code == 405
    assert response.json().get("status") == "error"
    assert response.json().get("description") == "this method should not be here"