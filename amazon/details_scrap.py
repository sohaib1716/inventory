import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
from googletrans import Translator
import json
import re

from googletrans import Translator

length = 21
k = 1

req = requests.get("https://amzn.to/3mcqoYr")
soup = BeautifulSoup(req.content, "html.parser")

print(soup)
