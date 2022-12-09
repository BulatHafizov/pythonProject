import requests
from requests import Response

response: Response = requests.get('https://postman-echo.com/get?userId=777')
response.json()
print(response.json())