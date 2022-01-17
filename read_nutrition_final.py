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
sheet1 = wb.add_sheet('nutrition', cell_overwrite_ok=True)

# Opening JSON file
f = open('listing_page2_50000.json', encoding="utf8")

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

first_heading = []
heading_array = []
calorie_array = []
amount_array = []


for i in data['data']['recipe']:
    jk = 0
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

            #  totalCalBox totalCalBoxMob col-md-12 col-12
            inside = soup.find_all("div", class_="totalCalBox totalCalBoxMob col-md-12 col-12")
            ins = soup.find_all("h6")

            for heading in ins:
                print("heading :: " + heading.text)
                first_heading.append(heading.text)
            print("first heading : " + str(first_heading))

            recipe_measurement = soup.find_all("div", class_="calLabel text-capitalize")
            for ing_me in recipe_measurement:
                print("calorie name :: " + ing_me.text)
                calorie_array.append(ing_me.text)
                video_aray.append(video)
                if jk < 4:
                    print("checking : " + str(first_heading[0]))
                    heading_array.append(first_heading[0])
                elif jk < 7:
                    print("checking : " + str(first_heading[1]))
                    heading_array.append(first_heading[1])
                elif jk < 8:
                    print("checking : " + str(first_heading[2]))
                    heading_array.append(first_heading[2])
                else:
                    print("checking : " + str(first_heading[3]))
                    heading_array.append(first_heading[3])
                print("jk jk : " + str(jk))
                jk = jk + 1
            print()

            recipe_ing = soup.find_all("label", class_="calCount")
            for ingredients in recipe_ing:
                amount_array.append(ingredients.text)
                print("calorie param :: " + ingredients.text)

    except:
        print("no data")

print("heading : " + str(heading_array))
print("calorie name array : " + str(calorie_array))
print("calorie param array : " + str(amount_array))
print("video array : " + str(video_aray))

print("heading " + str(len(heading_array)))
print("calorie name array " + str(len(calorie_array)))
print("calorie param array " + str(len(amount_array)))
print("video array : " + str(video_aray))

index = 0
index2 = 0

while index2 < len(calorie_array):
    sheet1.write(index, 0, '0')
    sheet1.write(index2, 1, video_aray[index2])
    sheet1.write(index2, 2, calorie_array[index2])
    sheet1.write(index2, 3, amount_array[index2])
    sheet1.write(index2, 4, heading_array[index2])
    index2 = index2 + 1


wb.save('page2_nutrients_video.xls')

# Closing file
f.close()
