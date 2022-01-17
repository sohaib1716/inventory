import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser

length = 21
k = 1

link_array = []

while k < length:
    req = requests.get("https://www.cookingcarnival.com/category/allrecipes/page/" + str(k) + "/")
    soup = BeautifulSoup(req.content, "html.parser")

    titles = soup.find_all("h2")
    link = soup.find_all(class_="entry-title-link", href=True)

    for lin in link:
        print(lin["href"])
        link_array.append(lin["href"])

    k = k + 1
    print(k)

print(len(link_array))
# for title in titles:
#     print(title.text)

# print(soup)
