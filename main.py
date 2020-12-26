from tqdm import tqdm
from utils import createCSVForCategory, getCategories, getBooksOfCategory

booksCategories = getCategories()

for category in tqdm(booksCategories):
    books = getBooksOfCategory(category["link"])
    createCSVForCategory(category["name"], books)
