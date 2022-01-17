import json
import time
# from translate import Translator
from googletrans import Translator
import requests
from bs4 import BeautifulSoup

# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('ing_page_4', cell_overwrite_ok=True)

# Opening JSON file
f = open('listing_page4_50000.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
k = 0
jk = 0
lm = 0
ing = 0
meas = 0


measurement_Array = []
ingredient_Array = []
video_aray = []
lll = 0

for i in data['data']['recipe']:
    try:
        isVideo = str(i['recipeFormat'])
        print("isVideo : " + str(isVideo))
        lll = lll + 1
        if isVideo == "video":
            title = str(i['title'])
            video = str(i['videos'][0])
            endUrl = str(i['slug'])

            req = requests.get("https://www.slurrp.com/recipes/" + endUrl)
            print("request : " + str(req))
            print("link : " + "https://www.slurrp.com/recipes/" + endUrl)

            soup = BeautifulSoup(req.content, "html.parser")

            recipe_measurement = soup.find_all("span", class_="qtyLabel")
            print("measurements : " + str(recipe_measurement))
            for measurement in recipe_measurement:
                print("measurings :: " + measurement.text)
                measurement_Array.append(measurement.text)
                video_aray.append(video)
            print("length of measurement : " + str(len(video_aray)))

            recipe_ing = soup.find_all("span", class_="itemLabel")
            print("recipees : " + str(recipe_ing))
            for ingredients in recipe_ing:
                print("ingredient :: " + ingredients.text)
                ingredient_Array.append(ingredients.text)
            print("length of ingredients : " + str(len(ingredient_Array)))
            print()
            k = k + 1


    except:
        print("no data")


print("measurement array " + str(measurement_Array))
print("ingredient array " + str(ingredient_Array))
print("video array " + str(video_aray))

print("measurement array " + str(len(measurement_Array)))
print("ingredient array " + str(len(ingredient_Array)))
print("video array " + str(len(video_aray)))

index = 0
index2 = 0

while index2 < len(ingredient_Array):
    sheet1.write(index, 0, '0')
    sheet1.write(index2, 1, video_aray[index2])
    sheet1.write(index2, 2, ingredient_Array[index2])
    index2 = index2 + 1


while index < len(measurement_Array):
    sheet1.write(index, 3, measurement_Array[index])
    sheet1.write(index, 4, "Ingredients")
    index = index + 1


wb.save('xlwt page_4_ingredients_videoformat.xls')

# Closing file
f.close()
