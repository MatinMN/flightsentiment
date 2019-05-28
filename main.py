from newsapi import NewsApiClient
from helper import *
from requests import get
from bs4 import BeautifulSoup
import os

newsapi = NewsApiClient(api_key='3d9b2341d48c4f28bbf4c34e10e0521e')

def get_sentiment():

    countries = get_countries()

    overall_results = {}

    for country in countries:
        query = ' AND (politics OR government OR public affairs OR state affairs OR diplomacy OR party OR parliament or minister OR law)'
        name = country['name']

        print("getting news for " + name)

        exists = os.path.isfile('data/'+name+'.json')


        if exists == False:
            all_articles = newsapi.get_everything(q= str(name) + str(query),
                                                sources='bbc-news, abc-news, al-jazeera-english, ary-news, cbs-news, cnbc, cnn, fox-news, google-news, independent, msnbc, nbc-news, news24, new-york-magazine, politico, reuters, the-hindu, the-new-york-times, the-washington-post',
                                                from_param='2019-04-28',
                                                to='2019-05-30',
                                                language='en',
                                                page=5)

            with open('data/'+name + '.json', 'w+') as outfile:  
                json.dump(all_articles, outfile)
        else:
            with open('data/'+name +'.json') as json_file:  
                print("data collected from json file")
                data = json.load(json_file)

            all_articles = data

        articles = all_articles['articles']

    

        url = articles[0]['url']
        response = get(url)
        html = BeautifulSoup(response.content, 'html.parser')
        article = html.get_text()
        article = " ".join(article.split())

        words_arr = article.split(" ")

        results = {}

        freq_arr = {}
        words_arr = remove_stopwords(words_arr)
        positive_freq = 0
        negetive_freq = 0
        print("counting words for " + name)
        for word in words_arr:
            if(len(word) < 10):

                if(word in freq_arr):
                    freq_arr[word.encode('utf-8').strip()] += 1
                else:
                    freq_arr[word.encode('utf-8').strip()] = 1
                if(word in POSITIVE_LIST):
                    positive_freq += 1
                if(word in NEGETIVE_LIST):
                    negetive_freq += 1

        results['word_freq'] = freq_arr
        results["negetive_score"] = negetive_freq
        results["positive_score"] = positive_freq


        overall_results[str(countries)] = results


    return overall_results

print get_sentiment()