import requests
import re
from bs4 import BeautifulSoup

baseUrl = "http://books.toscrape.com"
possibleRatings = ['One', 'Two', 'Three', 'Four', 'Five']

class Book:

	Url: str
	Name: str
	Description: str
	Category: str
	Upc: str
	Price: float
	PriceWithoutTax: float
	Availability: int
	Image: str
	Rating: str = "Zero"

	def __init__(self):
		pass

	def toDictionary(self):
		return {
			"product_page_url": self.Url,
			"title": self.Name,
			"product_description": self.Description,
			"category": self.Category,
			"universal_product_code": self.Upc,
			"price_including_tax": self.Price,
			"price_excluding_tax": self.PriceWithoutTax,
			"number_available": self.Availability,
			"review_rating": self.Rating,
			"image_url": self.Image
		}

	def getFromUrl(bookUrl: str):
		bookInstance = Book()
		finalUrl = "{}/{}".format(baseUrl, bookUrl)
		bookInstance.Url = finalUrl
		request = requests.get(finalUrl)
		soup = BeautifulSoup(request.content, 'html.parser')

		productPage = soup.find("article", class_="product_page")

		if productPage is None:
			return

		table = productPage.find("table", class_="table table-striped")

		if table is None:
			return

		# print(table.find_all('tr'));

		table = table.find_all('tr')

		bookInstance.Upc = table[0].td.string
		bookInstance.Price = float(table[3].td.string.replace('£', ''))
		bookInstance.PriceWithoutTax = float(table[2].td.string.replace('£', ''))
		bookInstance.Availability = int(re.search("([0-9]+) ([a-zA-Z]+)", table[5].td.string).group(1))
		bookInstance.Name = soup.find("div", class_="product_main").h1.text
		bookInstance.Image = baseUrl + soup.find("div", class_="carousel").div.div.div.img.attrs['src'].replace('../..', '')

		_tempRating = soup.find("p", class_="star-rating").attrs['class']
		for cls in _tempRating:
			if possibleRatings.count(cls) == 1:
				bookInstance.Rating = cls
				break
		bookInstance.Description = soup.find("div", id="product_description").next_sibling.next_sibling.text
		bookInstance.Category = str(soup.find("ul", class_="breadcrumb").contents[5].text).strip()

		return bookInstance

Book.getFromUrl = staticmethod(Book.getFromUrl)