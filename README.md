# Openclassrooms Project 2

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project aim to scrap books from http://books.toscrape.com website

## To start

### Requirements

- Python 3

### Installation

- Clone or download this repository, extract it inside a folder if necessary, then open a command prompt inside this folder.

- In the command prompt, create a new environment for the python project :

##### (You need the venv package from PiP to do it, if you don't have it, please write `pip install venv` to install it)

To create a new environment, write this command :

`virtualenv env`

Then you need to activate it :

```bash
cd env/Scripts

activate

cd ../..
```

And finally, you can install the required packages for the project :

`pip install -r requirements.txt`

## Usage

Inside the project folder run the command :

`py main.py`

Wait until the process end, then you will get a new folder called `data` which will contain few csv files (One for each category of books) containing all the data about the books like the UPC, the price ...

Inside the data folder, you will also get another folder called `images` containing some subfolders (One for each category) containing the covers of the books in the format `Name_of_the_book-UPC`

## Built with

- [Python](https://www.python.org/)
- [Beautiful Soup 4 Module](https://pypi.org/project/beautifulsoup4/)
- [Requests Module](https://pypi.org/project/requests/)
- [TQDM Module](https://pypi.org/project/tqdm/)