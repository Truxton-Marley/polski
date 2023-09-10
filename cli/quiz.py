import json

with open("temp_db") as file:
    words = json.load(file)

question = "Nie ma ___"

for word in words:
    word = json.loads(word)
    print(word["singular"]["mianownik"])
    print(question)
    response = input()
    answer = word["singular"]["dopełniacz"]
    if response == answer:
        print("\nDobrze!!!\n")
    else:
        print(response, answer)


