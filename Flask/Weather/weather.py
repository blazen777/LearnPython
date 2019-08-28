import requests

def weather_by_city(name):
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': 'e926bb3f6cc24ab690d75135192808',
        'q': name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru',
    }

    response = requests.get(url, params=params)
    weather = response.json()

    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == '__main__':
    print(weather_by_city('Moscow,Russia'))