import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
from googletrans import Translator

import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
recipe = wb.add_sheet('recipe')

inngr = Workbook()
ingredients_excel = inngr.add_sheet('ingredients')

length = 21
k = 1
j = 0

exl = 0

link_array = []

name_ingredient = []
amount_ingredient = []
unit_ingredient = []
video_array = []

while k < length:
    req = requests.get("https://www.cookingcarnival.com/category/allrecipes/page/" + str(k) + "/")
    soup1 = BeautifulSoup(req.content, "html.parser")

    titles = soup1.find_all("h2")
    link = soup1.find_all(class_="entry-title-link", href=True)

    for lin in link:
        print("data's : " + str(j))
        link_array.append(lin["href"])

        req = requests.get(lin["href"])
        soup = BeautifulSoup(req.content, "html.parser")

        # print(soup)

        image = soup.find_all("img")

        title = soup.find("title")

        video = soup.find("iframe")

        translator = Translator()
        hindi_name = translator.translate(title.text, dest='hi')

        time = soup.find_all("span", class_="wprm-recipe-time wprm-block-text-normal")

        data_id = soup.find("div", class_="wprm-recipe-container")

        try:
            servings = data_id.attrs['data-servings']
        except:
            servings = "N/A"

        serving_unit = soup.find("span",
                                 class_="wprm-recipe-servings-unit wprm-recipe-details-unit wprm-block-text-normal")

        calories = soup.find("span",
                             class_="wprm-recipe-details wprm-recipe-nutrition wprm-recipe-calories wprm-block-text-normal")
        calories_unit = soup.find("span",
                                  class_="wprm-recipe-details-unit wprm-recipe-nutrition-unit wprm-recipe-calories-unit wprm-block-text-normal")
        author_name = soup.find("span", class_="wprm-recipe-details wprm-recipe-author wprm-block-text-normal")

        cuisine = soup.find("span", class_="wprm-recipe-cuisine wprm-block-text-normal")

        # print("--------------------" + str(cuisine.text))

        meal_cat = soup.find("span", class_="wprm-recipe-course wprm-block-text-normal")

        try:
            print("video : " + video.attrs['data-lazy-src'])
            youtube_Video = video.attrs['data-lazy-src']
        except:
            print("No video")
            youtube_Video = "No"

        if youtube_Video != "No":

            print("Link : " + str(lin["href"]))
            embedded_link = lin["href"]
            try:
                print("image : " + image[9].attrs['src'])
                image = image[9].attrs['src']
            except:
                image = "N/A"

            # english title
            try:
                print("english title : " + title.text)
                english_title = title.text
            except:
                print("title")
                english_title = "N/A"

            # hindi name
            try:
                print("hindi name : " + str(hindi_name.text))
                hindi_name = hindi_name.text
            except:
                print("hindi name")
                hindi_name = "N/A"

            # meal category
            try:
                print("meal category : " + str(meal_cat.text))
                meal_cat = meal_cat.text
            except:
                print("no meal")
                meal_cat = "N/A"

            # time
            try:
                print("total time : " + str(time[2].text))
                making_time = time[2].text
            except:
                print("total time : " + str(time[0].text))
                making_time = time[0].text

            # servings
            try:
                print("serving : " + str(servings + " " + serving_unit.text))
                total_serving = servings + " " + serving_unit.text
            except:
                total_serving = "N/A"
                print("N/A")

            # calories
            try:
                print("calories : " + str(calories.text + " " + calories_unit.text))
                total_calories = calories.text + " " + calories_unit.text
            except:
                total_calories = "N/A"
                print("no calories")

            # author name
            try:
                author_title = author_name.text
                print("author name : " + str(author_name.text))
            except:
                author_title = "N/A"
                print("no author")

            # cuisine name
            try:
                print("cuisine : " + str(cuisine.text))
                new_cuisine = cuisine.text
            except:
                new_cuisine = "N/A"
                print("no cusine")

            recipe.write(exl, 0, '')  # id
            recipe.write(exl, 1, str(hindi_name))  # hindi title
            recipe.write(exl, 2, str(english_title))  # english title
            recipe.write(exl, 3, str(youtube_Video))  # youtube video
            recipe.write(exl, 4, str(image))  # image link
            recipe.write(exl, 5, str(total_serving))  # total servings
            recipe.write(exl, 6, str(making_time))  # total time
            recipe.write(exl, 7, '')  # rating
            recipe.write(exl, 8, str(meal_cat))  # meal(e.g breakfast, dinner)
            recipe.write(exl, 9, "veg")  # diet veg or non veg
            recipe.write(exl, 10, str(new_cuisine))  # cusine (e.g indian, american)
            recipe.write(exl, 11, str(author_title))  # source name
            recipe.write(exl, 12, str(''))  # related videos
            recipe.write(exl, 13, str(embedded_link))  # embedded link
            recipe.write(exl, 14, str(total_calories))  # embedded link

            exl = exl + 1

            ingredient_name = soup.find_all("span", class_="wprm-recipe-ingredient-name")
            ingredient_amount = soup.find_all("span", class_="wprm-recipe-ingredient-amount")
            ingredient_unit = soup.find_all("span", class_="wprm-recipe-ingredient-unit")

            temp = 0
            temp_check = 0

            for in_name in ingredient_name:
                print("ingredient name :: " + str(in_name.text))
                name_ingredient.append(in_name.text)
                video_array.append(video.attrs['data-lazy-src'])
                temp = temp + 1

            print("temp : " + str(temp))
            print("temp check : " + str(temp_check))

            while temp_check < temp:
                try:
                    print("ingredients_amount :: " + str(ingredient_amount[temp_check].text) + " " + str(
                        ingredient_unit[temp_check].text))
                    amount_ingredient.append(ingredient_amount[temp_check].text)
                    unit_ingredient.append(ingredient_unit[temp_check].text)
                except:
                    amount_ingredient.append("N/A")
                    unit_ingredient.append("N/A")
                temp_check = temp_check + 1

            j = j + 1
            print()

    k = k + 1
    print(k)

print(len(link_array))
print(name_ingredient)
print(amount_ingredient)
print(unit_ingredient)
print(video_array)

print(len(name_ingredient))
print(len(amount_ingredient))
print(len(unit_ingredient))
print(len(video_array))

v = 0



while v < len(name_ingredient):
    ingredients_excel.write(v, 0, '0')
    ingredients_excel.write(v, 1, str(video_array[v]))
    ingredients_excel.write(v, 2, str(name_ingredient[v]))
    ingredients_excel.write(v, 3, str(amount_ingredient[v] + " " + unit_ingredient[v]))
    ingredients_excel.write(v, 4, 'Ingredients')

    v = v + 1

# for title in titles:
#     print(title.text)

# print(soup)

inngr.save('dhwani_ingredients.xls')

wb.save('dhwani_recipees.xls')
