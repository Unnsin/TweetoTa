# ----------------------------------------------
# developer: Lesnoy V.S.
# Date: 15.03.2018
# Documentation:
# Version: 1.0
# ----------------------------------------------
import urllib.request
from bs4 import BeautifulSoup
import sys


class tweet:
    def __init__(self, name, text, url):
        self.Text = text;
        self.Name = name;
        self.URL = url;

class Parser(object):
    def __init__(self, file):
      self.tweets = []
      self.file = file      

    def getInitialTweets(self):
      for line in self.file:
        url = line
        buf = self.parse(self.get_html(url), url)
        self.tweets.append(buf)
      return self.tweets

    def get_html(self, url):
      response = urllib.request.urlopen(url);
      return response.read()

    def parse(self, html, url):
      soup = BeautifulSoup(html, "html.parser")
      tweetx = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
      name = soup.find("span", class_="username u-dir u-textTruncate")
      tweety = tweet(name.text, tweetx.text, url)
      return tweety
    
    def addAccount(self, string):
      self.file.append(string)

    def getAccounts(self):
      return self.file







# while(True):
#     for x in tweets:
#         buf = parse(get_html(x.URL))
#         if (buf.Text != x.Text):
#             print("UserName: "+ buf.Name)
#             print("Tweet: "+ buf.Text)
#             print("\n")
#             x.Text=buf.Text
