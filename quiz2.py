import json
from pprint import pprint

with open("temp_db") as file:
    words = json.load(file)

question = "Nie ma ___"

pprint(words)

for word in words.keys():
    print(words[word]["singular"]["mianownik"])
    print(question)
    response = input()
    answer = words[word]["singular"]["dopełniacz"]
    if response == answer:
        print("\nDobrze!!!\n")
    else:
        print(response, answer)


