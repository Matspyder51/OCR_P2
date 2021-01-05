from pathlib import Path
import shutil
from tqdm import tqdm
from utils import createCSVForCategory, getCategories, getBooksOfCategory

dataDir = Path("./data/")

if dataDir.exists():
    shutil.rmtree("./data/")

booksCategories = getCategories()

for category in tqdm(booksCategories):
    books = getBooksOfCategory(category["link"])
    createCSVForCategory(category["name"], books)
