import requests
import re
from bs4 import BeautifulSoup
from book import Book

def getCategories():
	categories = []
	request = requests.get("http://books.toscrape.com")
	soup = BeautifulSoup(request.content, 'html.parser')
	categoriesHtml = soup.find("div", class_="side_categories").ul.li.ul

	for category in categoriesHtml.find_all("a"):
		categories.append({"link": category.attrs["href"], "name": category.string.strip()})

	return categories

def getBooksOfCategory(category_link: str, current_getted_books = []):
	books = current_getted_books
	request = requests.get(category_link)
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

a = getBooksOfCategory("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
print(len(a))

# print(getCategories(), len(getCategories()))