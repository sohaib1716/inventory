import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
import json

from googletrans import Translator

length = 21
k = 1

link_array = []

req = requests.get("https://www.cookingcarnival.com/category/allrecipes/page/" + str(k) + "/")
soup = BeautifulSoup(req.content, "html.parser")

titles = soup.find_all("h2")
link = soup.find(class_="entry-title-link", href=True)

print(link["href"])
link_array.append(link["href"])

req = requests.get("https://www.cookingcarnival.com/cranberry-walnut-bread-no-knead-instant-pot-bread/")
soup = BeautifulSoup(req.content, "html.parser")

# print(soup)

image = soup.find_all("img")
print(image[9].attrs['src'])

title = soup.find("title")
print(title.text)

video = soup.find("iframe")

translator = Translator()
hindi_name = translator.translate(title.text, dest='hi')
print(hindi_name.text)

print(video.attrs['data-lazy-src'])

time = soup.find("span",
                 class_="wprm-recipe-details wprm-recipe-details-hours wprm-recipe-total_time wprm-recipe-total_time-hours")
unit = soup.find("span",
                 class_="wprm-recipe-details-unit wprm-recipe-details-unit-hours wprm-recipe-total_time-unit wprm-recipe-total_timeunit-hours")
serving = soup.find("span",
                    class_="wprm-recipe-servings wprm-recipe-details wprm-recipe-servings-18115 wprm-recipe-servings-adjustable-tooltip wprm-block-text-normal")
serving_unit = soup.find("span", class_="wprm-recipe-servings-unit wprm-recipe-details-unit wprm-block-text-normal")
calories = soup.find("span",
                     class_="wprm-recipe-details wprm-recipe-nutrition wprm-recipe-calories wprm-block-text-normal")
calories_unit = soup.find("span",
                          class_="wprm-recipe-details-unit wprm-recipe-nutrition-unit wprm-recipe-calories-unit wprm-block-text-normal")
author_name = soup.find("span", class_="wprm-recipe-details wprm-recipe-author wprm-block-text-normal")

cuisine = soup.find("span", class_="wprm-recipe-cuisine wprm-block-text-normal")

meal_cat = soup.find("span", class_="wprm-recipe-course wprm-block-text-normal")

print(meal_cat.text)
print(time)
print(unit)
print(serving)
print(serving_unit)
print(calories.text + " " + calories_unit.text)
print(author_name.text)
print(cuisine.text)

ingredient_name = soup.find_all("span", class_="wprm-recipe-ingredient-name")
ingredient_amount = soup.find_all("span", class_="wprm-recipe-ingredient-amount")
ingredient_unit = soup.find_all("span", class_="wprm-recipe-ingredient-unit")

for in_name in ingredient_name:
    print("ingredient name :: " + str(in_name.text))

for in_amount in ingredient_amount:
    print("ingredient amount :: " + str(in_amount.text))

for in_unit in ingredient_unit:
    print("ingredient unit :: " + str(in_unit.text))

# print(soup)
# wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-total_time wprm-recipe-total_time-minutes
# wprm-recipe-details wprm-recipe-details-hours wprm-recipe-total_time wprm-recipe-total_time-hours