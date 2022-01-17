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
ing_xls = wb.add_sheet('ingredients')

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

    try:
        video_id = json_Data["youtubeUrl"]
    except:
        video_id = "https://www.youtube.com/playlist?list=PLcotaVSEV1s9Zq9o0ZxPPJjoNJ6HDikJV"
    print("video url :: "+str(video_id))


    try:
        cat = json_Data["recipeIngredients"]
        print(cat[0]['group'])
        category_name = cat[0]['group']['name']

    except:
        category_name = "Ingredients"
    print(category_name)

    try:
        ingredients = json_Data['recipeIngredients'][0]['group']['ingredients']
        print("ingredients :  " + str(len(ingredients)))
        print("ingredients :  " + str(ingredients))
        lm = 0
        while lm < len(ingredients):
            name = ingredients[lm]['ingredient']
            quantity = ingredients[lm]['quantity']
            print("name : "  + str(name))
            print("quantity : " + str(quantity))

            ing_xls.write(k, 0, '0')
            ing_xls.write(k, 1, video_id)
            ing_xls.write(k, 2, name)
            ing_xls.write(k, 3, quantity)
            ing_xls.write(k, 4, category_name)

            k = k + 1
            lm = lm + 1


    except:
        print("sorry")

    print()

print("k : " + str(k))

wb.save('coockingshooking_ingredients.xls')
# Closing file
f.close()