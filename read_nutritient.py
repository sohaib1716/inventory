import requests
from bs4 import BeautifulSoup

req = requests.get("https://ranveerbrar.com/recipes/")
soup = BeautifulSoup(req.text, "html.parser")

recipe_title = soup.title
first_heading = []
heading_array = []
calorie_array = []
amount_array = []
jk = 0
print()
print(soup.prettify())
print()


top = soup.find("p").get_text()
print("top values : " + str(top))


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
    if jk < 4:
        print("checking : "+str(first_heading[0]))
        heading_array.append(first_heading[0])
    elif jk < 7:
        print("checking : "+str(first_heading[1]))
        heading_array.append(first_heading[1])
    elif jk < 8:
        print("checking : "+str(first_heading[2]))
        heading_array.append(first_heading[2])
    else:
        print("checking : "+str(first_heading[3]))
        heading_array.append(first_heading[3])
    print("jk jk : " + str(jk))
    jk = jk + 1
print()

recipe_ing = soup.find_all("label", class_="calCount")
for ingredients in recipe_ing:
    amount_array.append(ingredients.text)
    print("calorie param :: " + ingredients.text)

print("heading : " + str(heading_array))
print("calorie name array : " + str(calorie_array))
print("calorie param array : " + str(amount_array))