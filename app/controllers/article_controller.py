#!/usr/bin/python3
"""article retrieval and parsing moudule"""
import requests


def get_article(url, keyword):
    """get article from url"""
    response = requests.get(url, timeout=10000)
    articles = []

    if response.status_code == 200:
        dic = response.json()
        lst_articles = dic['Result']['Items']['Item']
        for article in lst_articles:
            print(article['Title'])
            article_title = article['Title']
            if keyword.lower() in article_title.lower():
                print("Article Title:", article_title)
                articles.append(article_title)

    print("Article Title:", article_title)
    return articles
