# ----------------------------------------------
# developer: Lesnoy V.S.
# Date:
# Time:
# Documentation: 
# ----------------------------------------------
import urllib.request
from bs4 import BeautifulSoup
import sys
filename = "sysname.txt"
file = open(filename, encoding="UTF-8", mode="r")


def get_html(url):
    response = urllib.request.urlopen(url);
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    tweet = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    name = soup.find("span", class_="username u-dir u-textTruncate")
    print("UserName: " + name.text)
    print("Tweet: " + tweet.text)


for line in file:
    url = line
    print(parse(get_html(url)))



