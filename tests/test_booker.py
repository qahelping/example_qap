from services.booker_service import BookerService


def test_booker_auth():
    booker = BookerService()
    response = booker.auth("admin", "password123")

    assert response['token']
