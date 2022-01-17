# importing libraries
from bs4 import BeautifulSoup
import requests


def main(URL):
    # opening our output file in append mode
    File = open("out.csv", "a")

    # specifying user agent, You can use other user agents
    # available on the internet
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit / 537.36(KHTML, like Gecko)Chrome / 44.0.2403.157Safari / 537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # retrieving product title
    try:
        # Outer Tag Object
        title = soup.find("span",
                          attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip().replace(',', '')

    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string)

    # saving the title in the file
    File.write(f"{title_string},")


    # product price
    # a - size - medium a - color - price priceblock_vat_excl_price
    try:
        # Outer Tag Object
        title = soup.find_all("span",
                          attrs={"class": 'a-offscreen'})

        print("testing :-")
        print(title)
        print("__________")

        # Inner NavigableString Object
        price = title.string

        # Title as a string value
        title_string = price.strip().replace(',', '')

    except AttributeError:
        price = "NA"
    print("price = ", price)


    # retrieving price
    try:
        price = soup.find(
            "span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
    # we are omitting unnecessary spaces
    # and commas form our string

    except AttributeError:
        price = "NA"
    print("Products price = ", price)


    try:
        rating = soup.find(
            "span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
    except:
        rating = "NA"
    print("Overall rating = ", rating)

    File.write(f"{rating},")

    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

    except AttributeError:
        review_count = "NA"
    print("Total reviews = ", review_count)
    File.write(f"{review_count},")

    # print availablility status
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')

    except AttributeError:
        available = "NA"
    print("Availability = ", available)

    # saving the availability and closing the line
    File.write(f"{available},\n")

    # closing the file
    File.close()

if __name__ == '__main__':
    # opening our url file to access URLs
    # file = open("url.txt", "r")

    # iterating over the urls
    # for links in file.readlines():
    main("https://www.amazon.in/INDIANA-ORGANIC-Homemade-Aamchi-Sandwich/dp/B089KKPJM6/ref=as_li_ss_tl?pd_rd_w=MzsWY&pf_rd_p=950901b9-b71e-4c33-9fc5-41ec6db58ad1&pf_rd_r=DCCTHCCSSM2BVD7WA6MA&pd_rd_r=454375f6-9386-4cbe-abef-1ee531cd9445&pd_rd_wg=ZzR9f&pd_rd_i=B089KKPJM6&psc=1&linkCode=sl1&tag=kickic-21&linkId=3b3d56bf5783fa069af71ba03524996b&language=en_IN")
