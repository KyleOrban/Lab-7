import requests
api = "1f7644968c944e1e969c257d4e2bc2fa"
url = "https://newsapi.org/v2/everything?q=USA&from=2025-04-01&sortBy=popularity&apiKey=1f7644968c944e1e969c257d4e2bc2fa"

try:
    response = requests.get(url)
    son = response.json()
    artcls = son.get("articles")
    mostpopular = artcls[0]
    print("Самая популярная статья, в которой упоминается США с 2 апреля по сегодня")
    print("заголовок: " + mostpopular.get("title"))
    print("дата: " + mostpopular.get("publishedAt"))
    print("источник: " + mostpopular.get("source").get("name"))
    print("описание: " + mostpopular.get("description"))
    print("начало статьи: " + (mostpopular.get("content")))
except:
    print("ошибка " + response.status_code)