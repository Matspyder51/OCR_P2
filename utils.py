import requests
import re
from bs4 import BeautifulSoup
from book import Book
from pathlib import Path
import csv

baseUrl = "http://books.toscrape.com"

def getCategories():
	categories = []
	request = requests.get(baseUrl)
	soup = BeautifulSoup(request.content, 'html.parser')
	categoriesHtml = soup.find("div", class_="side_categories").ul.li.ul

	for category in categoriesHtml.find_all("a"):
		categories.append({"link": category.attrs["href"], "name": category.string.strip()})

	return categories

def getBooksOfCategory(category_link: str, current_getted_books = []):
	books = current_getted_books
	request = requests.get("{}/{}".format(baseUrl, category_link))
	soup = BeautifulSoup(request.content, 'html.parser')
	pageList = soup.find("section").find("ol", class_="row")

	for book in pageList.find_all("li"):
		_b_data = book.article.h3.a
		bookInstance = Book.getFromUrl("catalogue/{}".format(_b_data.attrs["href"].replace("../", "")))
		books.append(bookInstance)

	pager = soup.find("ul", class_="pager")
	if pager and pager.find("li", class_="next"):
		next_page = pager.find("li", class_="next").a.attrs["href"]
		new_link = re.sub("/page-([0-9]+).html", "", category_link.replace("/index.html", ""))
		new_link = "{}/{}".format(new_link, next_page)
		return getBooksOfCategory(new_link, books)

	return books

def createCSVForCategory(category_name: str, books: list):
	imageDir = Path('./data/images/{}'.format(category_name))

	if not imageDir.exists():
		imageDir.mkdir(parents=True)

	with open('data/{}.csv'.format(category_name), 'w', encoding='utf-8', newline='') as csvfile:
		fieldnames = ["product_page_url", "title", "product_description", "category", "universal_product_code", "price_including_tax", "price_excluding_tax", "number_available", "review_rating", "image_url"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()

		for book in books:
			writer.writerow(book.toDictionary())
			response = requests.get(book.Image)

			file = open("./data/images/{}/{}-{}.jpg".format(category_name, book.Name.replace(':', '').replace(' ', '_'), book.Upc), "wb")
			file.write(response.content)
			file.close()