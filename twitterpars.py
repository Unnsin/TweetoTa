# ----------------------------------------------
# developer: Lesnoy V.S.
# Date:
# Time:
# Documentation:
# Version: 1.0
# ----------------------------------------------
import urllib.request
from bs4 import BeautifulSoup
import sys
filename = "sysname.txt"
file = open(filename, encoding="UTF-8", mode="r")

class tweet:
    def __init__(self, name, text, url):
        self.Text = text;
        self.Name = name;
        self.URL = url;

def get_html(url):
    response = urllib.request.urlopen(url);
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    tweetx = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    name = soup.find("span", class_="username u-dir u-textTruncate")
    tweety = tweet(name.text,tweetx.text,url)
    return tweety

tweets = [];
for line in file:
    url = line
    buf = parse(get_html(url))
    print("UserName: " + buf.Name)
    print("Tweet: " + buf.Text)
    tweets.append(buf)
    print("\n")
while(True):
    for x in tweets:
        buf = parse(get_html(x.URL))
        if (buf.Text != x.Text):
            print("UserName: "+ buf.Name)
            print("Tweet: "+ buf.Text)
            print("\n")
            x.Text=buf.Text
