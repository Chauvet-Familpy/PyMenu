from bs4 import BeautifulSoup
import urllib
from googletrans import Translator

url = "https://world.openfoodfacts.org/entry-date/2016-08/ingredients"

html_content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html_content, 'html.parser')

data = soup.findAll("a", {"class": "tag known"})

translator = Translator()

for i in data:
    print(translator.translate(i.text, dest="fr").text)