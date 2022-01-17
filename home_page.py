import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser


req = requests.get("https://www.slurrp.com/discover/recipes/")
soup = BeautifulSoup(req.content, "html.parser")

names = soup.find_all("div", class_="recipe-name-section")

for n in names:
    try:
        print(n.label.text)
    except:
        print()

driver = webdriver.Chrome(executable_path= r'C:\\Utility\\BrowserDrivers\\chromedriver.exe')

while True:
    next_page_btn = driver.find_element("//li[@class = 'pagination-next']/a")
    if len(next_page_btn) < 1:
        print("No more pages left")
        break
    else:
        print("heey")
