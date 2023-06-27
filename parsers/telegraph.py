import json
import requests


def make_request(url, params):
    response = requests.post(url, data=params)
    return json.loads(response.content)


def create_page(access_token, title, author_name, author_url, content, return_content=True):
    url = 'https://api.telegra.ph/createPage'
    params = {
        'access_token': access_token,
        'title': title,
        'content': content,
        'author_name': author_name,
        'author_url': author_url,
        'return_content': return_content
    }
    response = requests.post(url, data=params)
    data = json.loads(response.content)
    return data


def get_page_url(title, author_name, author_url, content):
    response = requests.get('https://api.telegra.ph/createAccount?short_name=Anton')
    token = json.loads(response.content)['result']['access_token']
    print(token)
    page = create_page(access_token=token, title=title, author_name=author_name, author_url=author_url, content=content)
    return page['result']['url']
