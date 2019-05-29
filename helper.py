import json
import re, string, unicodedata

STOPLIST = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]



def get_countries():
    with open('cities_with_id.json') as json_file:  
        data = json.load(json_file)
    return data['data']['cities']

def get_cities():
    with open('cities_with_name.json') as json_file:  
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
