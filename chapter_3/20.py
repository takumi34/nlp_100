import json

with open('jawiki-country.json', mode='r', encoding='utf-8') as f:
    for i in f:
        article = json.loads(i)
        if 'イギリス' == article['title']:
            print(article['text'])
