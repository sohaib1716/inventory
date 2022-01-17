import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
from googletrans import Translator
import json

from googletrans import Translator
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()
recipe = wb.add_sheet('recipe')

inngr = Workbook()
ingredients_excel = inngr.add_sheet('ingredients')

length = 32
k = 1
exl = 0

link_array = []

category_array = []
ingredients_array = []
video_link_array = []
tablespoon = []

# while k < 3:
# https://hebbarskitchen.com/recipes/biryani/page/2/?_gl=1%2A1ftbbv3%2A_ga%2AUmdQaDd0a1ZNbHhOR3ZVd3pfV2hrMXFvS2s5dzByVTJnSndWN1lqc3hacTJtc1FtQ190VkRUYm0yLU1CZm1UUQ


while (k < length):
    req = requests.get("https://hebbarskitchen.com/page/" + str(k) + "/?s=dessert")
    soup = BeautifulSoup(req.content, "html.parser")

    # h3 = soup.find("h3")
    array = ["td-image-wrap", "td-image-wrap td-module-video-modal"]

    for i in array:
        link = soup.find_all("a", class_=i, href=True)

        for li in link:
            print("--------------------------------------------------------------------")
            print(li['href'])

            req = requests.get(li['href'])
            home_page = BeautifulSoup(req.content, "html.parser")

            try:
                youtube = home_page.find("div", class_="rll-youtube-player")
                youtube = youtube.attrs["data-src"]
                print(youtube)
            except:
                youtube = "none"

            if (youtube != "none"):

                food_title = home_page.find("title").text
                print(food_title)

                translator = Translator()
                hindi_name = translator.translate(food_title, dest='hi')
                print(hindi_name.text)
                hind = hindi_name.text

                try:
                    image = home_page.find("img", class_="entered lazyloaded")
                except:
                    image = "none"
                print(image)

                try:
                    making_time = home_page.find_all("span", class_="wprm-recipe-time wprm-block-text-normal")
                    print(making_time[0].text)
                    time_make = making_time[0].text
                except:
                    making_time = "None"
                    print(making_time)
                    time_make = making_time

                # print(soup)

                try:
                    meal_type = home_page.find("span", class_="wprm-recipe-course wprm-block-text-normal")
                    print(meal_type.text)
                    mea = meal_type.text
                except:
                    mea = "dinner"

                try:
                    cuisine = home_page.find("span", class_="wprm-recipe-cuisine wprm-block-text-normal")
                    print(cuisine.text)
                    cui = cuisine.text
                except:
                    cui = "indian"

                try:
                    servings = home_page.find("span", class_="wprm-recipe-servings-with-unit")
                    print(servings.text)
                    ser = servings.text
                except:
                    ser = "3"

                try:
                    calories = home_page.find("span", class_="wprm-recipe-nutrition-with-unit")
                    print(calories.text)
                    cal = calories.text
                except:
                    calories = "NA"
                    cal = calories

                recipe.write(exl, 0, '')  # id
                recipe.write(exl, 1, str(hind))  # hindi title
                recipe.write(exl, 2, str(food_title))  # english title
                recipe.write(exl, 3, str(youtube))  # youtube video
                recipe.write(exl, 4, str(image))  # image link
                recipe.write(exl, 5, str(ser))  # total servings
                recipe.write(exl, 6, str(time_make))  # total time
                recipe.write(exl, 7, '')  # rating
                recipe.write(exl, 8, str(mea))  # meal(e.g breakfast, dinner)
                recipe.write(exl, 9, "veg")  # diet veg or non veg
                recipe.write(exl, 10, str(cui))  # cusine (e.g indian, american)
                recipe.write(exl, 11, str("Hebbars Kitchen"))  # source name
                recipe.write(exl, 12, str(''))  # related videos
                recipe.write(exl, 13, str(li['href']))  # embedded link
                recipe.write(exl, 14, str(cal))  # embedded link

                exl = exl + 1

                # calories = home_page.find("span", class_="wprm-recipe-nutrition-with-unit")
                # print(calories.text)

                ingredients_category = home_page.find_all("div", class_="wprm-recipe-ingredient-group")
                # print(ingredients_category)
                for ing_Cat in ingredients_category:
                    # print(ing_Cat)
                    category_name = ing_Cat.text.split(':')

                    cat_ofing = category_name[0]

                    print("lenght :: " + str(len(cat_ofing)))

                    if len(cat_ofing) > 100:
                        categ = "Ingredients"
                    else:
                        categ = cat_ofing

                    print("category :: " + str(categ))

                    try:
                        ingredients = category_name[1].split('▢')
                    except:
                        ingredients = category_name[0].split('▢')

                    for ing in ingredients:
                        print(ing)
                        x = ing.split()
                        print(x)

                        try:
                            print("table spoon  :: " + str(x[0] + " " + x[1]))
                            tb = x[0] + " " + x[1]
                            tablespoon.append(tb.lstrip())
                            n = 2
                            add = ""
                            while n <= len(x):
                                print("n : " + str(n))
                                print("x : " + str(len(x)))
                                add = add + " " + x[n]
                                print("add :: " + str(add.lstrip()))
                                l = len(x)
                                if n == l-1 :
                                    print("hello bhai")
                                    ingredients_array.append(str(add.lstrip()))
                                    print("ing array :: " + str(ingredients_array))
                                n = n + 1
                        except:
                            print("no array")

                        video_link_array.append(youtube)
                        try:
                            category_array.append(categ)
                        except:
                            category_array.append("")

                print("--------------------------------------------------------------------")

    k = k + 1

v = 0

print("length of video : " + str(len(video_link_array)))
print("length of ingredients : " + str(len(ingredients_array)))
print("length of category : " + str(len(category_array)))

print("video : " + str(video_link_array))
print("ingredients : " + str(ingredients_array))
print("category : " + str(category_array))

while v < len(ingredients_array):
    ingredients_excel.write(v, 0, '0')
    ingredients_excel.write(v, 1, str(video_link_array[v]))
    ingredients_excel.write(v, 2, str(ingredients_array[v]))
    ingredients_excel.write(v, 3, str(tablespoon[v]))
    ingredients_excel.write(v, 4, str(category_array[v]))

    v = v + 1

# for title in titles:
#     print(title.text)

# print(soup)

inngr.save('dessert_ingredient.xls')

wb.save('dessert_recipe.xls')
