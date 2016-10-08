from lxml import html
import requests

page = requests.get('http://localhost:8888/index.html')
tree = html.fromstring(page.content)

print(tree.tag)

