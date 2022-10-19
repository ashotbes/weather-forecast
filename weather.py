import requests

API_KEY = '272b76523addab3c4a44a6f00139aa22'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Hi! Please enter your city name \n")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    temperature = round(data['main']['temp'] - 273.15, 0)
    weather = data['weather'][0]['description']

    print(f'Weather: {weather}')
    print(f'Temperature: {temperature} °C')
else:
    print("An error occurred with link :c ")

