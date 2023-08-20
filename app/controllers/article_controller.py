#!/usr/bin/python3
"""article retrieval and parsing moudule"""
import requests


def get_article(url):
    """get article from url"""
    response = requests.get(url)
    if response.status_code == 200:
        dict = response.json()
        lst_articles = dict['Result']['Items']['Item']
        for article in lst_articles:
            print(article['Id'])
            print(article['Title'])


if __name__ == '__main__':
    get_article('https://health.gov/myhealthfinder/api/v3/itemlist.json?Type=topic')