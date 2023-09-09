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
    przymiotnik_dict = {}
    przymiotnik_dict[query] = {}
    przymiotnik_dict[query]['singular'] = {}
    przymiotnik_dict[query]['singular']['mianownik'] = {}
    przymiotnik_dict[query]['singular']['dopełniacz'] = {}
    przymiotnik_dict[query]['singular']['celownik'] = {}
    przymiotnik_dict[query]['singular']['biernik'] = {}
    przymiotnik_dict[query]['singular']['narzędnik'] = {}
    przymiotnik_dict[query]['singular']['miejscownik'] = {}
    przymiotnik_dict[query]['singular']['wołacz'] = {}
    przymiotnik_dict[query]['plural'] = {}
    przymiotnik_dict[query]['plural']['mianownik'] = {}
    przymiotnik_dict[query]['plural']['dopełniacz'] = {}
    przymiotnik_dict[query]['plural']['celownik'] = {}
    przymiotnik_dict[query]['plural']['biernik'] = {}
    przymiotnik_dict[query]['plural']['narzędnik'] = {}
    przymiotnik_dict[query]['plural']['miejscownik'] = {}
    przymiotnik_dict[query]['plural']['wołacz'] = {}

    odmiana = soup.table
    odmiana = soup.find_all("table", class_="odmiana")[0]
    # Skip table headers and comparatives [2:9]
    for row in odmiana.find_all('tr')[2:9]:
        grammar_case = row.a.get('title')
        if grammar_case == 'mianownik' or grammar_case == 'wołacz':
            singular_m = (row.find_all('td')[1].string)
            przymiotnik_dict[query]['singular'][grammar_case]['ma'] = singular_m
            singular_f = (row.find_all('td')[2].string)
            singular_n = (row.find_all('td')[3].string)
            plural_m = (row.find_all('td')[4].string)
            plural_nm = (row.find_all('td')[5].string)
        elif grammar_case == 'biernik':
            singular_ma = (row.find_all('td')[1].string)
            przymiotnik_dict[query]['singular'][grammar_case]['ma'] = singular_ma
            singular_m = (row.find_all('td')[2].string)
            singular_f = (row.find_all('td')[3].string)
            singular_n = (row.find_all('td')[4].string)
            plural_m = (row.find_all('td')[5].string)
            plural_nm = (row.find_all('td')[6].string)
        else:
            singular_m = (row.find_all('td')[1].string)
            przymiotnik_dict[query]['singular'][grammar_case]['ma'] = singular_m
            singular_f = (row.find_all('td')[2].string)
            singular_n = (row.find_all('td')[3].string)
            plural_m = (row.find_all('td')[4].string)
            plural_nm = (row.find_all('td')[4].string)
        przymiotnik_dict[query]['singular'][grammar_case]['m'] = singular_m
        przymiotnik_dict[query]['singular'][grammar_case]['f'] = singular_f
        przymiotnik_dict[query]['singular'][grammar_case]['n'] = singular_n
        przymiotnik_dict[query]['plural'][grammar_case]['m'] = plural_m
        przymiotnik_dict[query]['plural'][grammar_case]['nm'] = plural_nm

    meaning = soup.find_all(string=re.compile("angielski:"))[0].parent.a.text
    przymiotnik_dict[query]['meaning'] = meaning 
    print(przymiotnik_dict)
else:
    print("Opps! Something went wrong...we did not get back a 200")


przymiotnik_json = json.dumps(przymiotnik_dict)

# temporary flat file for database; TODO: convert to SQL
with open("przymiotnik_temp_db", "r+") as file:
    db = file.read()
    db_py = json.loads(db)
    print(db_py)
    file.seek(0)
    file.truncate()
    db_py[query] = przymiotnik_dict[query]
    file.write(json.dumps(db_py))


