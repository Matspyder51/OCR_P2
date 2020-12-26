import requests
import re
from bs4 import BeautifulSoup

baseUrl = "http://books.toscrape.com"
possibleRatings = ["One", "Two", "Three", "Four", "Five"]


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

    soupData: BeautifulSoup

    def __init__(self):
        pass

    def getBaseInformations(self):
        self.Name = self.__soupData.find("div", class_="product_main").h1.text
        try:
            self.Description = self.__soupData.find(
                "div", id="product_description"
            ).next_sibling.next_sibling.text
        except AttributeError:
            self.Description = "None"
        self.Category = str(
            self.__soupData.find("ul", class_="breadcrumb").contents[5].text
        ).strip()

    def getAdvancedInformations(self):

        productPage = self.__soupData.find("article", class_="product_page")

        if productPage is None:
            return

        table = productPage.find("table", class_="table table-striped")

        if table is None:
            return

        table = table.find_all("tr")

        self.Upc = table[0].td.string
        self.Price = float(table[3].td.string.replace("£", ""))
        self.PriceWithoutTax = float(table[2].td.string.replace("£", ""))
        self.Availability = int(
            re.search("([0-9]+) ([a-zA-Z]+)", table[5].td.string).group(1)
        )

    def getRating(self):
        _tempRating = self.__soupData.find(
            "p",
            class_="star-rating"
        ).attrs["class"]
        for cls in _tempRating:
            if possibleRatings.count(cls) == 1:
                self.Rating = cls
                break

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
            "image_url": self.Image,
        }

    @staticmethod
    def getFromUrl(bookUrl: str):
        bookInstance = Book()
        bookInstance.Url = "{}/{}".format(baseUrl, bookUrl)
        request = requests.get(bookInstance.Url)
        if not request.ok:
            return

        bookInstance.__soupData = BeautifulSoup(request.content, "html.parser")

        bookInstance.getBaseInformations()
        bookInstance.getAdvancedInformations()
        bookInstance.getRating()

        bookInstance.Image = baseUrl + bookInstance.__soupData.find(
            "div", class_="carousel"
        ).div.div.div.img.attrs["src"].replace("../..", "")

        return bookInstance


Book.getFromUrl = staticmethod(Book.getFromUrl)
