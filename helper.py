import json
import re, string, unicodedata
import os
from requests import get
from bs4 import BeautifulSoup
STOPLIST = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]



def get_news_articles(name):

    exists = os.path.isfile('data/'+name+'.json')
    query = ' AND (politics OR government OR public affairs OR state affairs OR diplomacy OR party OR parliament or minister OR law)'

    if exists == False:
        all_articles = newsapi.get_everything(q= str(name) + str(query),
                                            sources='bbc-news, abc-news, al-jazeera-english, ary-news, cbs-news, cnbc, cnn, fox-news, google-news, independent, msnbc, nbc-news, news24, new-york-magazine, politico, reuters, the-hindu, the-new-york-times, the-washington-post',
                                            from_param='2019-05-10',
                                            to='2019-05-30',
                                            language='en',
                                            page=5)

        with open('data/'+name + '.json', 'w+') as outfile:  
            json.dump(all_articles, outfile)
        return all_articles
    else:
        with open('data/'+name +'.json') as json_file:  
            print("data collected from json file")
            data = json.load(json_file)
            return data



def get_countries():
    with open('cities_with_id.json') as json_file:  
        data = json.load(json_file)
    return data['data']['cities']

def get_cities():
    with open('cities_with_names.json') as json_file:  
        data = json.load(json_file)
    return data['data']['cities']


def loadPositiveWords():
    with open('positiveWords.json') as json_file:  
        data = json.load(json_file)
    return data

def loadNegetiveWords():
    with open('negetiveWords.json') as json_file:  
        data = json.load(json_file)
    return data


def rabin_karp(pattern, text):

    p_len = len(pattern)
    p_hash = hash(pattern)

    for i in range(0, len(text) - (p_len - 1)):

        # written like this t
        text_hash = hash(text[i:i + p_len])
        if text_hash == p_hash and \
                text[i:i + p_len] == pattern:
            return True
    return False


def remove_stopwords(words):

    new_words = []
    stop_words = ' '.join(STOPLIST)
    for word in words:
        if(rabin_karp(word,stop_words) == False):
            new_words.append(word)

    return new_words

POSITIVE_LIST = loadPositiveWords()
NEGETIVE_LIST = loadNegetiveWords()


def get_positivity_score(name,url,results,id):
    
        exists = os.path.isfile('data/'+name+'-article'+str(id)+'.html')
        if exists:
            
            with open('data/'+name +'-article'+str(id)+'.html') as article_file:  
                html = BeautifulSoup(article_file.read(), 'html.parser')
        else:
            
            print("downaloding")
            response = get(url,stream=True)    
            html = BeautifulSoup(response.content, 'html.parser')
            with open('data/'+name + '-article'+str(id)+'.html', 'w+') as article_file:  
                article_file.write(response.content)
                
        article = html.get_text()

        article = " ".join(article.split())

        words_arr = article.split(" ")

        freq_arr = results['word_freq']
        
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

        words_arr = remove_stopwords(words_arr)

        results['word_freq'] = freq_arr
        print(positive_freq)
        
        results["negative"] += negetive_freq
        results["positive"] += positive_freq
        print(results["positive"])
        return results
       
