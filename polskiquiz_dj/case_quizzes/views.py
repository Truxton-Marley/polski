from django.http import HttpResponse
from django.shortcuts import render
import json
#import os

#wd = os.getcwd()
with open ("./case_quizzes/adjectives_temp_db") as file:
    adjectives_json = file.read()

slownik = {
    "nadwaga": "overweight",
    "zapał": "enthusiasm",
    "szron": "hoarfrost",
    "objczaj": "custom, tradition",
}

# Create your views here.

def index(request):
    return render(request, "case_quizzes/cases.html", {
        "slownik": slownik,
        "js_slownik": json.dumps(slownik),
        "adjectives": adjectives_json,
    })

# Samples:
def test(request):
    return render(request, "case_quizzes/index.html", {
        "slownik": slownik,
        "js_slownik": json.dumps(slownik),
        "adjectives": adjectives_json,
    })

def lookup(request, word):
    return HttpResponse(f"<h1>{word} to znaczy '{slownik.get(word)}'</h1>")

def chwytny(request):
    return HttpResponse("<h1>Chwytny to znaczy 'Prehensile'</h1>")

