import json
import os
import random
import time
from pprint import pprint

with open("noun_temp_db") as file:
    nouns = json.load(file)

with open("adjectives_temp_db") as file:
    adjectives = json.load(file)

gender_mapping_singular = {
    "nijaki": "n",
    "żeński": "f",
    "męskorzeczowy": "m",
    # ma = masculine alive, maybe not the best choice of wording...
    "męskoosobowy": "ma",
    "męskozwierzęcy": "ma",
}

gender_mapping_plural = {
    # nm: non-living masculine, m: masculine :
    # should really be mp: masculine persion, o: other...potential todo at some point
    "nijaki": "nm",
    "żeński": "nm",
    "męskorzeczowy": "nm",
    "męskoosobowy": "m",
    "męskozwierzęcy": "nm",
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
    response = input("\n")
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
        if number == "singular":
            answer = adjectives[adjective][number][przypadek][gender_mapping_singular[gender]]
            adjective_nomnitive = adjectives[adjective][number]["mianownik"][gender_mapping_singular[gender]]
        elif number == "plural":
            answer = adjectives[adjective][number][przypadek][gender_mapping_plural[gender]]
            adjective_nomnitive = adjectives[adjective][number]["mianownik"][gender_mapping_plural[gender]]
        answer += " "
        answer += nouns[word][number][przypadek]
        response = ""
        while response != answer:
            print(f'{adjective_nomnitive} {nouns[word][number]["mianownik"]}')
            response = ask_question(question)
            if response == answer:
                print("\nDobrze!!!\n")
            else:
                print(f"Twoja odpowiedz: {response}\nCorrect answer: {answer}\n\n")
    time.sleep(2)
    os.system("clear")

question_sets = [
    # Singular
    {"questions": questions_genitive, "przypadek": "dopełniacz", "number":"singular"},
    {"questions": questions_dative, "przypadek": "celownik", "number":"singular"},
    {"questions": questions_accusative, "przypadek": "biernik", "number":"singular"},
    {"questions": questions_instrumental, "przypadek": "narzędnik", "number":"singular"},
    {"questions": questions_locative, "przypadek": "miejscownik", "number":"singular"},
    {"questions": questions_vocative, "przypadek": "wołacz", "number":"singular"},
    # Plural
    {"questions": questions_genitive, "przypadek": "dopełniacz", "number":"plural"},
    {"questions": questions_dative, "przypadek": "celownik", "number":"plural"},
    {"questions": questions_accusative, "przypadek": "biernik", "number":"plural"},
]

ask_questions(**random.choice(question_sets))
ask_questions(questions_genitive, "dopełniacz")
ask_questions(questions_genitive, "dopełniacz", number="plural")
ask_questions(questions_locative, "miejscownik")
ask_questions(questions_locative, "miejscownik", number="plural")

#for question in question_sets:
#    ask_questions(**question)


#ask_questions(questions_instrumental, "narzędnik")
#ask_questions(questions_locative, "miejscownik", number="plural")
#ask_questions(questions_locative, "miejscownik")
#ask_questions(questions_genitive, "dopełniacz", number="plural")
#ask_questions(questions_accusative, "biernik")
#ask_questions(questions_vocative, "wołacz")

