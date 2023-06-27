import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import pyshorteners


def get_headlines(category):
    url = "https://techcrunch.com/category/" + category
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("h2", class_="post-block__title")
        translator = GoogleTranslator(source='auto', target='ru')
        headlines = [(translator.translate(article.find("a").text.strip()), pyshorteners.Shortener().tinyurl.short(article.find("a")["href"]))
                     for article in articles]
        return headlines
    else:
        print(f"Ошибка: {response.status_code}")
