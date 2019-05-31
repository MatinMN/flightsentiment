from __future__ import division
from newsapi import NewsApiClient
from helper import *
from requests import get
from bs4 import BeautifulSoup
import os

newsapi = NewsApiClient(api_key='3d9b2341d48c4f28bbf4c34e10e0521e')


def get_sentiment():

    countries = get_countries()

    overall_results = {}

    for i in range(1,len(countries)):

        country = countries[i]
        
        name = country['name']

        print("getting news for " + name)

        
        all_articles = get_news_articles(name)
        
        articles = all_articles['articles']

        results = {}

        results['word_freq'] = {}
        results["negative"] = 0
        results["positive"] = 0

        for i in range(1):
            url = articles[i]['url']

            results = get_positivity_score(name,url,results,i)

        
        
        overall_results[str(name)] = results
    return overall_results

