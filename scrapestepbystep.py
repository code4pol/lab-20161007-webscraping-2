from lxml import html
import requests

page = requests.get('file:///Users/alegomes/code/unb/code4pol/lab-20161007-webscraping-2/index.html')
print(page)