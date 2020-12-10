import requests
import re
from bs4 import BeautifulSoup

baseUrl = "http://books.toscrape.com"
possibleRatings = ['One', 'Two', 'Three', 'Four', 'Five']

def getBookData(bookUrl: str):
	finalUrl = "{}/{}".format(baseUrl, bookUrl)
	request = requests.get(finalUrl)
	soup = BeautifulSoup(request.content, 'html.parser')

	productPage = soup.find("article", class_="product_page")

	if productPage is None:
		return False

	table = productPage.find("table", class_="table table-striped")

	if table is None:
		return False

	# print(table.find_all('tr'));

	table = table.find_all('tr')

	upc = table[0].td.string
	priceNoTax = float(table[2].td.string.replace('£', ''))
	priceTax = float(table[3].td.string.replace('£', ''))
	availability = int(re.search("([0-9]+) ([a-zA-Z]+)", table[5].td.string).group(1))
	name = soup.find("div", class_="product_main").h1.text
	image = baseUrl + soup.find("div", class_="carousel").div.div.div.img.attrs['src'].replace('../..', '')
	_tempRating = soup.find("p", class_="star-rating").attrs['class']
	rating = 'Zero'
	for cls in _tempRating:
		if possibleRatings.count(cls) == 1:
			rating = cls
			break
	description = soup.find("div", id="product_description").next_sibling.next_sibling.text
	category = str(soup.find("ul", class_="breadcrumb").contents[5].text).strip()
	return True, upc, priceNoTax, priceTax, name, availability, image, rating, description, category, finalUrl