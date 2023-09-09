import json
import os
import random
import time
from pprint import pprint

with open("noun_temp_db") as file:
    nouns = json.load(file)

with open("adjectives_temp_db") as file:
    adjectives = json.load(file)

gender_mapping = {
    "nijaki": "n",
    "żeński": "f",
    "męskorzeczowy": "m",
    # ma = masculine alive, maybe not the best choice of wording...
    "męskoosobowy": "ma",
    "męskozwierzęcy": "ma",
}

questions_genitive = [
    "Nie ma ___",
    "Jakie jest pani zdanie na temat ___",
    "brakuje mi ___",
    "Ona bardzo boi się ___",
    ]

questions_locative = [
    "Co pan myśli o ___",
    "Co pani sądzi o ___",
    ]

questions_instrumental = [
    "Bardzo tęskie za ___",
    "Ty jesteś ___",
    ]

questions_accusative = [
    "Ja widzę ___",
    "My mamy ___",
    ]

questions_dative = [
    "Zgłaszam protest przeciw ___",
    "Wy dajecie prezent ___",
    ]

questions_vocative = [
    "O, ___!",
    ]

praise = [
    "Dobrze!!!",
    "Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił.",
]

pprint(nouns)
pprint(adjectives)

def ask_question(question):
    print(question)
    response = input()
    return response

def ask_questions(questions, przypadek, number="singular"):
    print("################################################################################")
    print(f"                           {przypadek}   :   {number}                     ")
    print("################################################################################")
    
    all_nouns = [word for word in nouns.keys()]
    all_adjectives = [word for word in adjectives.keys()]
    quiz_nouns = [random.choice(all_nouns) for i in range(10)]
    quiz_adjectives = [random.choice(all_adjectives) for i in range(10)]
    for word, adjective in zip(quiz_nouns, quiz_adjectives):
        question = random.choice(questions)
        gender = nouns[word]["gender"]
        answer = adjectives[adjective][number][przypadek][gender_mapping[gender]]
        answer += " "
        answer += nouns[word][number][przypadek]
        response = ""
        while response != answer:
            print(f'{adjectives[adjective][number]["mianownik"]["m"]} {nouns[word][number]["mianownik"]}')
            response = ask_question(question)
            if response == answer:
                print("\nDobrze!!!\n")
            else:
                print(response, answer)
    time.sleep(2)
    os.system("clear")

question_sets = [
    {"questions": questions_genitive, "przypadek": "dopełniacz", "number":"singular"},
    {"questions": questions_dative, "przypadek": "celownik", "number":"singular"},
    {"questions": questions_accusative, "przypadek": "biernik", "number":"singular"},
    {"questions": questions_instrumental, "przypadek": "narzędnik", "number":"singular"},
    {"questions": questions_locative, "przypadek": "miejscownik", "number":"singular"},
    {"questions": questions_vocative, "przypadek": "wołacz", "number":"singular"},
]

ask_questions(**random.choice(question_sets))
ask_questions(questions_genitive, "dopełniacz")

#for question in question_sets:
#    ask_questions(**question)


#ask_questions(questions_instrumental, "narzędnik")
#ask_questions(questions_locative, "miejscownik", number="plural")
#ask_questions(questions_locative, "miejscownik")
#ask_questions(questions_genitive, "dopełniacz", number="plural")
#ask_questions(questions_accusative, "biernik")
#ask_questions(questions_vocative, "wołacz")

