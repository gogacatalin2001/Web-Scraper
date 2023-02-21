from bs4 import BeautifulSoup, NavigableString, Tag
import requests

amp_url = "https://www.thomann.de/ro/fender_reissue_blues_deluxe_gitarrencombo.htm"
thomann_home_url = "https://www.thomann.de/intl/index.html"

result = requests.get(thomann_home_url).text
doc = BeautifulSoup(result, "html.parser")

# TODO populate the categories - DONE
# TODO get the links of the categories - DONE
# TODO access the desired category and subcategories until a leaf category is found
# TODO search for the desired item
# TODO monitor it's price and availability
# TODO notify when the desired item is n stock or when the desired price is reached or other criteria is met


# Get the instrument categories

# get the grid that contains the categories
category_grid = doc.find("div", class_=["fx-category-grid"])
categories = category_grid.contents
# create the (title, link) tuples for every category for facilitating navigation
category_items = []
# for cat in categories:
sibling = categories[0].next_sibling
while sibling is not None:
    if isinstance(sibling, Tag):
        title = sibling['title']
        link = sibling['href']
        category_items.append((title, link))
    sibling = sibling.next_sibling

print(category_items)


