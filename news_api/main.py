import requests


def news_api(q):
    url = requests.get(f'https://newsapi.org/v2/everything?q={q}&from=2023-01-05&sortBy=popularity&apiKey'
                       '=d4790b6e2b374c80a680422d8d0afe56')
    content = url.json()
    articles = content['articles']
    for article in articles:
        print("Title:\n", article['title'], "\nDescription:\n", article['description'])


news_api('Apple')
