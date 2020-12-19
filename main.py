from book import Book
from utils import createCSVForCategory, getCategories, getBooksOfCategory

b1 = Book.getFromUrl("catalogue/a-light-in-the-attic_1000/index.html")

# createCSVForCategory('Poetry', [b1])

booksCategories = getCategories()

for category in booksCategories:
	books = getBooksOfCategory(category['link'])
	createCSVForCategory(category['name'], books)

# print(
# 	"{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".
# 		format(
# 			b1.Name,
# 			b1.PriceWithoutTax,
# 			b1.Price,
# 			b1.Upc,
# 			b1.Image,
# 			b1.Rating,
# 			b1.Category,
# 			b1.Url,
# 			b1.Description
# 		)
# )