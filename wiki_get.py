import re
import requests
import sys
from bs4 import BeautifulSoup

#with open('kot') as file:
#    slowo = file.read()

url_base = "https://pl.wiktionary.org/wiki/"
query = sys.argv[1]
url = url_base + query

response = requests.get(url)
print(response.status_code)

if (response.status_code == 200):
    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.prettify())


    # Create dictionary to hold nouns
    rzeczownik_json = {}
    rzeczownik_json['singular'] = {}
    rzeczownik_json['plural'] = {}

    odmiana = soup.table
    odmiana = soup.find_all("table", class_="odmiana")[0]
    for row in odmiana.find_all('tr')[1:]:
        grammar_case = row.a.get('title')
        singular = (row.find_all('td')[1].string)
        plural = (row.find_all('td')[2].string)
        rzeczownik_json['singular'][grammar_case] = singular
        rzeczownik_json['plural'][grammar_case] = plural

    meaning = soup.find_all(string=re.compile("angielski"))[0].parent.a.text
    rzeczownik_json['meaning'] = meaning 
    print(rzeczownik_json)
else:
    print("Opps! Something went wrong...we did not get back a 200")

