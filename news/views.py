from django.shortcuts import render

# Create your views here.

import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)


# indian express
ie_r = requests.get("https://indianexpress.com/section/india/")
ie_soup = BeautifulSoup(ie_r.content, 'html.parser')
ie_headings = ie_soup.findAll('h2', {"class": "title"})
# ht_headings = ht_headings[:-23]
ie_news = []

for ieh in ie_headings:
    ie_news.append(ieh.text)

# hindustan times

ht_r = requests.get("https://www.news18.com/india/")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll('h4', {"class": "jsx-3328680553"})
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ie_news': ie_news, 'ht_news': ht_news})