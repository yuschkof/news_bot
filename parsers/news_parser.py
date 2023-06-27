import json
from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator
from parsers.telegraph import get_page_url


def translate_text(text):
    return GoogleTranslator(source='auto', target='ru').translate(text)


def get_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title_element = soup.find('h1', class_='article__title')
    title = title_element.text if title_element else ''
    author_element = soup.find('div', {'class': 'article__byline'}).find('a')
    author = author_element.text if author_element else ''
    image_element = soup.find('img', {'class': 'article__featured-image'})
    content = soup.find('div', class_='article-content').find_all(['p', 'div', 'h2'])

    nodes = [
        {
            "tag": "p",
            "children": [
                {
                    "tag": "a",
                    "attrs": {"href": url},
                    "children": ["Оригинал статьи"]
                }
            ]
        },
        {
            "tag": "figure",
            "children": [
                {"tag": "img", "attrs": {"src": image_element["src"]}}
            ]
        }
    ]

    for item in content:
        if item.name == 'p' and 'wp-caption-text' not in item.get('class', []):
            nodes.append({
                "tag": "p",
                "children": [translate_text(item.text)]
            })
        elif item.name == 'div' and item.find('img'):
            img_tag = item.find('img')
            img_src = img_tag['src']
            caption_tag = item.find('p', class_='wp-caption-text')
            caption_text = caption_tag.text if caption_tag else ''
            nodes.append({
                "tag": "figure",
                "children": [
                    {"tag": "img", "attrs": {"src": img_src}},
                    {"tag": "figcaption", "children": [translate_text(caption_text)]}
                ]
            })
        elif item.name == 'h2':
            nodes.append({
                "tag": "h3",
                "children": [translate_text(item.text)]
            })

    content_json = json.dumps(nodes)
    return get_page_url(translate_text(title), author, author_element['href'], content_json)
