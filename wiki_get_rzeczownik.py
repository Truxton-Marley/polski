import json
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
    rzeczownik_dict = {}
    rzeczownik_dict[query] = {}
    rzeczownik_dict[query]['singular'] = {}
    rzeczownik_dict[query]['plural'] = {}

    odmiana = soup.table
    odmiana = soup.find_all("table", class_="odmiana")[0]
    for row in odmiana.find_all('tr')[1:]:
        grammar_case = row.a.get('title')
        singular = (row.find_all('td')[1].string)
        plural = (row.find_all('td')[2].string)
        rzeczownik_dict[query]['singular'][grammar_case] = singular
        rzeczownik_dict[query]['plural'][grammar_case] = plural

    meaning = soup.find_all(string=re.compile("angielski:"))[0].parent.a.text
    rzeczownik_dict[query]['meaning'] = meaning 

    #gender = soup.p.i.string.split()[2]
    gender = soup.find(string=re.compile("rzeczownik, rodzaj ")).split()[2]
    rzeczownik_dict[query]['gender'] = gender 

    print(rzeczownik_dict)
else:
    print("Opps! Something went wrong...we did not get back a 200")


rzeczownik_json = json.dumps(rzeczownik_dict)

# temporary flat file for database; TODO: convert to SQL
with open("noun_temp_db", "r+") as file:
    db = file.read()
    db_py = json.loads(db)
    print(db_py)
    file.seek(0)
    file.truncate()
    db_py[query] = rzeczownik_dict[query]
    file.write(json.dumps(db_py))


