import requests
from requests import Response

response: Response = requests.post('https://postman-echo.com/post', json=dict(userId='777', username='Bulat'))
json_response = response.json()
print(response.json())