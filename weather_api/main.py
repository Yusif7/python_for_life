import requests


def weather_app(city):
    url = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={city},us&mode=json&appid=a673b52d7151c7b4c096dc0b54cd08b9')
    content = url.json()
    results = []
    count = 1
    for i in range(len(content)):
        results.append(
            city + ', ' + content['list'][i]['dt_txt'] + ', ' + content['list'][i]['weather'][0]['description'])
    with open('data.txt', 'w') as f:
        f.write(str(count) + ' ' + 'City, ' + 'Time, ' + 'Condition' + '\n')
        for weather in results:
            count += 1
            f.write(str(count) + ' ' + weather + '\n')




weather_app('London')
