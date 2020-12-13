from book import Book

b1 = Book.getFromUrl("catalogue/a-light-in-the-attic_1000/index.html")

print(
	"{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".
		format(
			b1.Name,
			b1.PriceWithoutTax,
			b1.Price,
			b1.Upc,
			b1.Image,
			b1.Rating,
			b1.Category,
			b1.Url,
			b1.Description
		)
)