import requests


def test_userid_good():
    response = requests.get('https://postman-echo.com/get?userId=777')
    response_body = response.json()
    assert response_body["args"]["userId"] == "777"
