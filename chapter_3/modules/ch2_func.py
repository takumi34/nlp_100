import json


def extract_uk_text():
    with open('jawiki-country.json', mode='r', encoding='utf-8') as f:
        for i in f:
            article = json.loads(i)
            if 'イギリス' == article['title']:
                return article['text']
