import json
import os
import random
import time
from pprint import pprint

with open("noun_temp_db") as file:
    words = json.load(file)

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

pprint(words)

def ask_question(question):
    print(question)
    response = input()
    return response

def ask_questions(questions, przypadek, number="singular"):
    print("################################################################################")
    print(f"                           {przypadek}   :   {number}                     ")
    print("################################################################################")
    
    all_words = [word for word in words.keys()]
    print(all_words)
    quiz_words = [random.choice(all_words) for i in range(10)]
    for word in quiz_words:
        question = random.choice(questions)
        answer = words[word][number][przypadek]
        response = ""
        while response != answer:
            print(words[word][number]["mianownik"])
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

ask_questions(questions_genitive, "dopełniacz")
ask_questions(questions_genitive, "dopełniacz")
#ask_questions(**random.choice(question_sets))

#for question in question_sets:
#    ask_questions(**question)


#ask_questions(questions_instrumental, "narzędnik")
#ask_questions(questions_locative, "miejscownik", number="plural")
#ask_questions(questions_locative, "miejscownik")
ask_questions(questions_genitive, "dopełniacz", number="plural")
#ask_questions(questions_accusative, "biernik")
#ask_questions(questions_vocative, "wołacz")

