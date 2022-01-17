import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.slurrp.com/recipes/aloo-methi-recipe-dry-aloo-methi-recipe-1621595545")
soup = BeautifulSoup(req.content, "html.parser")

recipe_title = soup.title
recipe_time = soup.find("span", class_="foodInfoLabel")
recipe_servings = soup.find("span", class_="serveOpt")
recipe_ingredients = soup.find("ul", class_="requiredIngredient")
link = soup.find("link", rel="canonical")



print("link : " + str(link.get("href")))
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


# testing = soup.find_all("div", class_="recipe-name-section")
#
# for test in testing:
#     try:
#         print(test.label.text)
#     except:
#         print()


# print(soup.prettify())
# print(soup.get_text())