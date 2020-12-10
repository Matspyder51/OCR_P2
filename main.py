from scrapper import getBookData

try:
	bookExist, bookUpc, bookPriceNoTax, bookPriceTax, bookName, bookAvailability, bookImage, bookRating, bookDescription, bookCategory, bookUrl = getBookData("catalogue/a-light-in-the-attic_1000/index.html")

	print(
		"{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".
			format(
			bookName,
			bookPriceNoTax,
			bookPriceTax,
			bookUpc,
			bookImage,
			bookRating,
			bookCategory,
			bookUrl,
			bookDescription
		)
	)
except TypeError:
	print('Error')