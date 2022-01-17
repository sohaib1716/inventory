import requests
from bs4 import BeautifulSoup

req2 = requests.get("https://www.slurrp.com/discover/recipes/")

soup = BeautifulSoup(req2.content, "html.parser")
recipe_time = soup.find_all("div", class_="overlay-wrap")


print(recipe_time)
array = []

for div in recipe_time:
    print(div.find('a')['href'])
    end_url = div.find('a')['href']
    array.append(end_url)

print(array)


for a in array:
    try:
        print("https://www.slurrp.com" + a)
        req = requests.get("https://www.slurrp.com" + str(a))


        soup = BeautifulSoup(req.content, "html.parser")

        recipe_title = soup.title
        recipe_time = soup.find("span", class_="foodInfoLabel")
        recipe_servings = soup.find("span", class_="serveOpt")
        recipe_ingredients = soup.find("ul", class_="requiredIngredient")

        print("title :: " + recipe_title.text)
        print("time :: " + recipe_time.text)
        print("Servings :: " + recipe_servings.text)
        print()
        # print(recipe_ingredients.prettify())

        recipe_measurement = soup.find_all("span", class_="qtyLabel")
        for ing_me in recipe_measurement:
            print("measurings :: " + ing_me.text)
        print()
        recipe_ing = soup.find_all("span", class_="itemLabel")
        for ingredients in recipe_ing:
            print("items used :: " + ingredients.text)

        print()
    except:
        print()

