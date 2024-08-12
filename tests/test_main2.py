import pytest
import requests
import json
import requests
import logging


def create_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    file_handler = logging.FileHandler("requests.log")
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    return logger


logger = create_logger()


def test_api_example():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"

    response = requests.get(url)
    response_dict = response.json()
    assert response.status_code == 200

    assert response_dict[0]["postId"] == 1
    assert response_dict[0]["id"] == 1
    assert response_dict[0]["name"] == "id labore ex et quam laborum"
    assert response_dict[0]["email"] == "Eliseo@gardner.biz"
    body = "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

    logger.warning("Watch out!")
    assert response_dict[0]["body"] == body


def test_api_payload():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": "1"}
    response = requests.get(url, params=params)
    response_dict = response.json()
    assert response.status_code == 200
    assert response.url == "https://jsonplaceholder.typicode.com/comments?postId=1"

    assert response_dict[0]["postId"] == 1
    assert response_dict[0]["id"] == 1
    assert response_dict[0]["name"] == "id labore ex et quam laborum"
    assert response_dict[0]["email"] == "Eliseo@gardner.biz"
    body = "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

    assert response_dict[0]["body"] == body


def test_api_response():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": "1"}
    response = requests.get(url, params=params)

    assert response.json()
    assert response.text
    assert response.status_code == 200
    assert response.url == "https://jsonplaceholder.typicode.com/comments?postId=1"


def test_api_json():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": "1"}
    response = requests.get(url, params=params)
    json = response.json()
    assert json[0]["postId"] == 1
    assert json[0]["id"] == 1
    assert json[0]["name"] == "id labore ex et quam laborum"
    assert json[0]["email"] == "Eliseo@gardner.biz"
    body = "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

    assert json[0]["body"] == body


def test_api_json_2():
    url = "https://api.thecatapi.com/v1/images/search"
    params = {"limit": "5"}
    response = requests.get(url, params=params)
    json = response.json()

    assert json[0]["id"]
    assert json[0]["url"]
    assert json[0]["width"]
    assert json[0]["height"]


@pytest.mark.parametrize("code", [202, 404, 401, 503])
def test_api_status_code(code):
    url = "https://httpbin.org/status/" + str(code)
    response = requests.get(url)
    print(response.text)
    assert response.status_code == code


@pytest.mark.parametrize("code", [202, 404, 401, 503])
def test_api_raise_for_status(code):
    url = "https://httpbin.org/status/" + str(code)
    response = requests.get(url)

    try:
        response.raise_for_status()
        logger.info("Запрос выполнен!")
        assert True
    except requests.exceptions.HTTPError as err:
        logger.error(f"Ошибка HTTP: {err}")
        assert False


@pytest.mark.parametrize("code", [410, 404, 401, 503])
def test_api_codes(code):
    url = "https://httpbin.org/status/" + str(code)
    response = requests.get(url)

    assert response.status_code == requests.codes.gone


def test_api_2_find_pet_by_id():
    url = "https://petstore.swagger.io/v2/pet/1"

    response = requests.get(url)
    json = response.json()

    assert response.status_code == 200
    assert json["id"] == 1
    assert json["category"]["id"] == 1
    assert json["category"]["name"] == "cat"
    assert json["name"] == "dog"
    assert json["photoUrls"] == []
    assert json["tags"] == []
    assert json["status"] == "sold"


def test_api_body():
    url = "https://petstore.swagger.io/v2/store/order"
    body = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-08-01T17:22:17.269Z",
        "status": "placed",
        "complete": True,
    }
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(body)
    response = requests.post(url, data=payload, headers=headers)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["id"]
    assert response_json["petId"] == body["petId"]
    assert response_json["quantity"] == body["quantity"]
    assert response_json["status"] == body["status"]
    assert response_json["complete"] == body["complete"]


def test_post_store_order():
    url = "https://petstore.swagger.io/v2/store/order"
    body = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-08-01T17:21:57.535Z",
        "status": "placed",
        "complete": True,
    }
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(body)

    response = requests.post(url, data=payload, headers=headers)
    json1 = response.json()
    assert response.status_code == 200
    assert json1["id"]
    assert json1["petId"] == body["petId"]
    assert json1["quantity"] == body["quantity"]
    assert json1["shipDate"] == body["shipDate"]
    assert json1["status"] == body["status"]
    assert json1["complete"] == body["complete"]


def test_api_headers():
    url = "https://petstore.swagger.io/v2/store/order"
    body = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-08-01T17:22:17.269Z",
        "status": "placed",
        "complete": True,
    }
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    payload = json.dumps(body)
    response = requests.post(url, data=payload, headers=headers)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["id"]
    assert response_json["petId"] == body["petId"]
    assert response_json["quantity"] == body["quantity"]
    assert response_json["status"] == body["status"]
    assert response_json["complete"] == body["complete"]
