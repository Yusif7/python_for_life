import requests


def weather_app(city):
    url = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=a673b52d7151c7b4c096dc0b54cd08b9')
    content = url.json()
    results = []
    count = 1
    # Extract the information which we need to and add it to the list
    for i in range(len(content)):
        results.append(
            city + ', ' + content['list'][i]['dt_txt'] + ', ' + content['list'][i]['weather'][0]['description'])
    # Extract from list and to data.txt file
    with open('data.txt', 'w') as f:
        f.write(str(count) + ' ' + 'City, ' + 'Time, ' + 'Condition' + '\n')
        for weather in results:
            count += 1
            f.write(str(count) + ' ' + weather + '\n')




weather_app('Baku')
