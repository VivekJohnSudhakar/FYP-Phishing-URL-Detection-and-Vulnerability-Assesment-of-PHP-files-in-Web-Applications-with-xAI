import sys
sys.path.append("C:/Users/Sriram/AppData/Local/Programs/Python/Python39/Lib/site-packages")

import pandas as pd
import numpy as np
import re
#import tldextract
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px
import requests
import whois
import dnstwist
from nltk.tokenize import RegexpTokenizer # regexp tokenizers use to split words from text
from nltk.stem.snowball import SnowballStemmer # stemmes words
from sklearn.feature_extraction.text import CountVectorizer # create sparse matrix of words using regexptokenizes

import pickle# use to dump model
from sklearn.svm import LinearSVC


#def main():
f = open("phishing.txt","w")
#url = 'www.yahoo.com'
url = sys.argv[1];

    # Add schema
if url[:4] != "http":
    url = "http://"+url
try:
    response = requests.get(url)
    f.write("URL is valid and exists on the internet\n")
except requests.ConnectionError as exception:
    f.write("URL does not exist on Internet\n")

    # Dealing with tiny URLs
    #Tiny url - URL = "http://shorturl.at/ajxEM"

r = requests.head(url = url,allow_redirects = True)
    #f.write(r.status_code)
    #f.write("\n")
if url != r.url:
    f.write("Input is a tiny url\n")
    f.write("The redirected links are :\n")
    for response in r.history:
        f.write(response.url)
        f.write("\n")
    f.write("The expanded URL is : " + r.url)
    url = r.url
    f.write("\n")
else:
    f.write("Input is not a tiny url\n")


    #Dont need whois data

    #print("Related information about the given URL: ")
    # Whois information
domain = whois.whois(url)
f.write(str(domain))
f.write("\n")
f.write("Passing URL through phishing detection\n")

filename = "C:/xampp/htdocs/FYP2/first_module/linearSVC_model_url_detec3.sav"
with open(filename, "rb") as fout:
    cv, loaded_model = pickle.load(fout)


tokenizer = RegexpTokenizer(r'[A-Za-z]+') #to getting alpha only
url_tokenized = tokenizer.tokenize(url) # tokenizing all the rows

stemmer = SnowballStemmer("english") # choose a language
url_stemmed = [stemmer.stem(word) for word in url_tokenized]
url_sent = ' '.join(url_stemmed) # joining the words in the list as a string

url_sent = [url_sent]
    # CountVectorizer is used to transform a corpora of text to a vector of term / token counts of each word.
    #cv = CountVectorizer(url_sent)
feature = cv.transform(url_sent) #transform all text which we tokenize and stemed

res = loaded_model.predict(feature)
if res[0] == "good":
    f.write(url + " is not a phishing URL")
else:
    f.write(url + " is a phishing URL")

f.close()

print('Complete')

    #x = True
    #return bool(x)




#if __name__ == "__main__":
#    main()
