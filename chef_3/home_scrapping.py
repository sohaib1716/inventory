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

link_array = []

# while k < 3:
# https://hebbarskitchen.com/recipes/biryani/page/2/?_gl=1%2A1ftbbv3%2A_ga%2AUmdQaDd0a1ZNbHhOR3ZVd3pfV2hrMXFvS2s5dzByVTJnSndWN1lqc3hacTJtc1FtQ190VkRUYm0yLU1CZm1UUQ
req = requests.get("https://hebbarskitchen.com/veg-fried-rice-vegetable-fried-rice/")
soup = BeautifulSoup(req.content, "html.parser")

link = soup.find(class_="td-image-wrap", href=True)

# for inside_link in link:
#     # print(inside_link["href"])

req = requests.get(link["href"])
home_page = BeautifulSoup(req.content, "html.parser")

food_title = home_page.find("title").text
print(food_title)

translator = Translator()
hindi_name = translator.translate(food_title, dest='hi')
print(hindi_name.text)

youtube = home_page.find("div", class_="rll-youtube-player")
youtube = youtube.attrs["data-src"]
print(youtube)

image = home_page.find("img", class_="entered lazyloaded")
print(image)

making_time = home_page.find_all("span", class_="wprm-recipe-time wprm-block-text-normal")
print(making_time[0].text)
# print(soup)

meal_type = home_page.find("span", class_="wprm-recipe-course wprm-block-text-normal")
print(meal_type.text)

cuisine = home_page.find("span", class_="wprm-recipe-cuisine wprm-block-text-normal")
print(cuisine.text)

servings = home_page.find("span", class_="wprm-recipe-servings-with-unit")
print(servings.text)

calories = home_page.find("span", class_="wprm-recipe-nutrition-with-unit")
print(calories.text)

ingredients_category = home_page.find_all("div", class_="wprm-recipe-ingredient-group")
for ing_Cat in ingredients_category:
    category_name = ing_Cat.text.split(':')
    print(category_name[0])
    ingredients = category_name[1].split('▢')

    for ing in ingredients:
        print(ing)

        temp = re.findall(r'\d+', ing)
        res = list(map(int, temp))

        # print result
        print("The numbers list is : " + str(res))

k = k + 1
