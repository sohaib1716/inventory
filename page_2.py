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
recipe = wb.add_sheet('recipe')


# Opening JSON file
f = open('small.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)


# Iterating through the json
# list
k = 0
ing = 0
meas = 0
url_array = []
for i in data['data']['recipe']:
    try:
        title = str(i['title'])
        servings = str(i['servingSize'])
        totaltime = str(i['totalTime'])
        video = str(i['videos'][0])
        endUrl = str(i['slug'])
        sourceName = str(i['sourceName'])
        video_array = str(i['videos'])

        print("current value : " + str(k))
        print("https://www.slurrp.com/recipes/"+str(endUrl))
        req = requests.get("https://www.slurrp.com/recipes/"+endUrl)
        print("request : " + str(req))
        soup = BeautifulSoup(req.text, "html.parser")
        link = soup.find("link", rel="canonical")
        print("link : " + str(link.get("href")))


        url_array.append(endUrl)

        translator = Translator()
        translation = translator.translate(title, dest='hi')

        dietType = str(i['dietPreference'][0])
        if dietType == "5fec725c85b2c132a4458437":
            diet = "veg"
        elif dietType == "5fec725c85b2c132a445843b":
            diet = "non veg"
        elif dietType == "5fec725c85b2c132a4458439":
            diet = "jain"
        elif dietType == "5fec725c85b2c132a445843a":
            diet = "Eggetarian"
        elif dietType == "5fec6abf75462d0e8c8b9cad":
            diet = "vegan"
        elif dietType == "5fec6abf75462d0e8c8b9cac":
            diet = "Keto"
        elif dietType == "5fec725c85b2c132a4458435":
            diet = "Paleo"
        elif dietType == "5fec725c85b2c132a4458434":
            diet = "Atkins"
        else:
            diet = "veg"


        mealType = str(i['mealType'][0])
        if mealType == "5fec6abf75462d0e8c8b9ca8":
            meal = "LD"
        elif mealType == "5fec6abf75462d0e8c8b9ca7":
            meal = "Brunch"
        elif mealType == "5fec6abf75462d0e8c8b9ca6":
            meal = "Breakfast"
        elif mealType == "5fec6abf75462d0e8c8b9cb4":
            meal = "Snack"
        elif mealType == "6020e6889ca95a47792c5263":
            meal = "Sea food"
        elif mealType == "5fec6abf75462d0e8c8b9cab":
            meal = "Salad"
        elif mealType == "5fec6abf75462d0e8c8b9cac":
            meal = "starter & appetizer"
        elif mealType == "5fec6abf75462d0e8c8b9caa":
            meal = "Soup"
        elif mealType == "5fec6abf75462d0e8c8b9cb1":
            meal = "Deserts"
        elif mealType == "5fec6abf75462d0e8c8b9cad":
            meal = "Main Course"
        else:
            meal = "LD"


        cusineCat = str(i['cuisineId'])
        if cusineCat == "5fec5400dae5e451af9925c1":
            cuisine = "Indian"
        elif cusineCat == "5fec5400dae5e451af9925f5":
            cuisine = "Rajasthani"
        elif cusineCat == "5fec5400dae5e451af9925c2":
            cuisine = "North Indian"
        elif cusineCat == "5fec5400dae5e451af9925ca":
            cuisine = "Punjabi"
        elif cusineCat == "5fec5400dae5e451af9925ed":
            cuisine = "Gujarati"
        elif cusineCat == "5fec5400dae5e451af9925f2":
            cuisine = "Bengali"
        elif cusineCat == "5fec5400dae5e451af9925b2":
            cuisine = "Chinese"
        elif cusineCat == "5fec5400dae5e451af9925c8":
            cuisine = "Uttar Pradesh"
        elif cusineCat == "5fec5400dae5e451af9925f3":
            cuisine = "Odia"
        elif cusineCat == "5fec5400dae5e451af992602":
            cuisine = "Vietnamese"
        elif cusineCat == "5fec5400dae5e451af9925af":
            cuisine = "Burmese"
        elif cusineCat == "5fec5400dae5e451af992629":
            cuisine = "Russian"
        elif cusineCat == "5fec5400dae5e451af99260f":
            cuisine = "African"
        elif cusineCat == "5fec5400dae5e451af992633":
            cuisine = "Mediterranean"
        elif cusineCat == "5fec5400dae5e451af992636":
            cuisine = "Italian"
        elif cusineCat == "5fec5400dae5e451af9925e1":
            cuisine = "Andhra"
        elif cusineCat == "5fec5400dae5e451af99263f":
            cuisine = "Australian"
        elif cusineCat == "5fec5400dae5e451af99264f":
            cuisine = "South American"
        elif cusineCat == "5fec5400dae5e451af992601":
            cuisine = "Thai"
        elif cusineCat == "5fec5400dae5e451af9925cb":
            cuisine = "Mughlai"
        elif cusineCat == "5fec5400dae5e451af9925eb":
            cuisine = "Maharashtrian"
        elif cusineCat == "5fec5400dae5e451af9925d3":
            cuisine = "Karnataka"
        elif cusineCat == "5fec5400dae5e451af99263e":
            cuisine = "Swiss"
        elif cusineCat == "5fec5400dae5e451af992600":
            cuisine = "Malaysian"
        elif cusineCat == "5fec5400dae5e451af992607":
            cuisine = "Lebanese"
        elif cusineCat == "5fec5400dae5e451af9925d1":
            cuisine = "Kerala"
        elif cusineCat == "5fec5400dae5e451af99263c":
            cuisine = "Dutch"
        elif cusineCat == "5fec5400dae5e451af9925bd":
            cuisine = "Korean"
        elif cusineCat == "5fec5400dae5e451af992603":
            cuisine = "Middle Eastern"
        elif cusineCat == "5fec5400dae5e451af992622":
            cuisine = "German"
        elif cusineCat == "5fec5400dae5e451af992634":
            cuisine = "Greek"
        elif cusineCat == "5fec5400dae5e451af99263a":
            cuisine = "Spanish"
        elif cusineCat == "5fec5400dae5e451af9925c3":
            cuisine = "Kashmiri"
        elif cusineCat == "5fec5400dae5e451af9925cc":
            cuisine = "Awadhi"
        elif cusineCat == "5fec5400dae5e451af9925d0":
            cuisine = "South Indian"
        elif cusineCat == "5fec5400dae5e451af99263d":
            cuisine = "French"
        elif cusineCat == "5fec5400dae5e451af992642":
            cuisine = "Mexican"
        elif cusineCat == "5fec5400dae5e451af992643":
            cuisine = "American"
        elif cusineCat == "5fec5400dae5e451af9925bc":
            cuisine = "Japanese"
        elif cusineCat == "5fec5400dae5e451af9925da":
            cuisine = "Tamil"
        elif cusineCat == "5fec5400dae5e451af992650":
            cuisine = "Brazilian"
        elif cusineCat == "5fec5400dae5e451af9925e2":
            cuisine = "Goan"
        elif cusineCat == "5fec5400dae5e451af992604":
            cuisine = "Arab"
        elif cusineCat == "5fec5400dae5e451af992617":
            cuisine = "Moroccan"
        elif cusineCat == "5fec5400dae5e451af992635":
            cuisine = "Turkish"
        else:
            cuisine = "Indian"


        recipe.write(k, 0, '')
        recipe.write(k, 1, translation.text)
        recipe.write(k, 2, title)
        recipe.write(k, 3, video)
        recipe.write(k, 4, '')
        recipe.write(k, 5, servings)
        recipe.write(k, 6, totaltime + str(" Mins"))
        recipe.write(k, 7, '')
        recipe.write(k, 8, meal)
        recipe.write(k, 9, diet)
        recipe.write(k, 10, cuisine)
        recipe.write(k, 11, sourceName)
        recipe.write(k, 12, video_array)
        recipe.write(k, 13, str(link.get("href")))



        print(translation.text)
        print(title)
        print(servings)
        print(totaltime)
        print(video)
        print(endUrl)
        print()

        k = k+1



    except:
        print("no data")

qw = 0

print("length of array = " + str(len(url_array)))
# while qw < len(url_array):
#     try:
#         print("current value : " + str(qw))
#         print("https://www.slurrp.com/recipes/"+str(url_array[qw]))
#         req = requests.get("https://www.slurrp.com/recipes/"+url_array[qw])
#         soup = BeautifulSoup(req.content, "html.parser")
#         link = soup.find("link", rel="canonical")
#         print("link : " + str(link.get("href")))
#         recipe.write(qw, 13, str(link.get("href")))
#     except:
#         recipe.write(qw, 13, '')
#     qw = qw + 1

wb.save('xlwt pre_Test2.xls')
# Closing file
f.close()