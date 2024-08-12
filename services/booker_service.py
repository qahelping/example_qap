from services.base_service import BaseService


class BookerService(BaseService):
    def __init__(self):
        super().__init__()
        self.url = "https://restful-booker.herokuapp.com/"

    def auth(self, login, password):
        body = {"username": login, "password": password}
        url = self.url + "auth"

        return self.post_request(url=url, body=body)
