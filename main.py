from utils import createCSVForCategory, getCategories, getBooksOfCategory

booksCategories = getCategories()

for category in booksCategories:
    print("Generating Category: {}".format(category["name"]))
    books = getBooksOfCategory(category["link"])
    createCSVForCategory(category["name"], books)
