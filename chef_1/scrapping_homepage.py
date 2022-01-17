import json
# from translate import Translator
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import lxml
import cchardet

# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
recipe = wb.add_sheet('coockingshooking')

# Opening JSON file
f = open('cookingshooking.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
k = 0
url_array = []


for json_Data in data["_collections"][0]["_data"]:
    english_name = json_Data["title"].replace('-', ' ')
    print(english_name)

    translator = Translator()
    hindi_name = translator.translate(english_name, dest='hi')
    print(hindi_name.text)

    try:
        video_id = json_Data["youtubeUrl"]
    except:
        video_id = "https://www.youtube.com/playlist?list=PLcotaVSEV1s9Zq9o0ZxPPJjoNJ6HDikJV"
    print("video url :: "+str(video_id))


    try:
        image = json_Data["recipeIntros"][0]["imageUrl"]
    except:
        image = "no image"
    print("dish image :: "+str(image))

    try:
        time = json_Data["totalTime"]
    except:
        time = "null"
    print("coocking time :: "+str(time))

    try:
        servings = json_Data["serves"]
    except:
        servings = "null"
    print("servings :: "+str(servings))

    try:
        chef = json_Data["author"]
    except:
        chef = "cookingshooking"
    print("chef name :: " + str(chef))

    try:
        link = "https://cookingshooking.com/"+json_Data["slug"]
    except:
        link = "https://cookingshooking.com/"
    print("redirect link :: " + str(link))

    recipe.write(k, 0, '')
    recipe.write(k, 1, hindi_name.text)
    recipe.write(k, 2, english_name)
    recipe.write(k, 3, video_id)
    recipe.write(k, 4, image)
    recipe.write(k, 5, servings)
    recipe.write(k, 6, time)
    recipe.write(k, 7, '')
    recipe.write(k, 8, 'meal')
    recipe.write(k, 9, 'diet')
    recipe.write(k, 10, 'cuisine')
    recipe.write(k, 11, chef)
    recipe.write(k, 12, '')
    recipe.write(k, 13, link)

    try:
        meal_category = json_Data["categories"]
        for cat in meal_category:
            print("categories : " + str(cat["category"]))
    except:
        print("nothing")

    print()
    k = k + 1

print("k : " + str(k))

wb.save('coockingshooking_recipees.xls')


# Closing file
f.close()