import json
import os
import requests

try:
    city_name = input("Введите город:")
    os.system('cls')
    key = "d05cfdf277cce5a535db89ab25b1f314"
    data = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
    results = json.loads(data.text)

    print(f"Погода в городе {city_name}!\n"
    f"Погода: {results['weather'][0]['main']}\n"
    f"Температура: {round(results['main']['temp'] -273)}°C (чувствуется как {round(results['main']['feels_like']-273)}°C)\n"
    f"Влажность: {results['main']['humidity']} %\n"
    f"Скорость ветра: {results['wind']['speed']} м/с\n"
    f"Давление: {results['main']['pressure']} hPa\n"
    )
except KeyError:
    print("Извините, мы не смогли найти ваш город :(\n")