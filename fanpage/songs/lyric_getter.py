import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.metrolyrics.com/everything-has-changed-lyrics-taylor-swift.html")

soup = BeautifulSoup(r.content, "html.parser")

with open('everything_has_changed.txt', 'w') as f:

	for tag in soup.find_all('p'):

		f.write(tag.text)