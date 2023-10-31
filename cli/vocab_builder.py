import random
from colorama import Fore, init
from slowa_vocab_builder import vocab, new_vocab, brand_new_vocab
from zacheta import zacheta

init(autoreset=True)

print(vocab)
print()

#####################################################################

def praise(zecheta):
    """Return encouragement or famous Polish quotes. Also the Lord's
    Prayer as you will hear this in Poland at weddings and funerals,
    so good to know."""
    print(Fore.GREEN + f"\n{random.choice(zacheta)}\n")

#####################################################################

def multiple_choice(vocab):
    keys = [key for key in vocab.keys()]
    key = random.choice(keys)
    answer = vocab[key]
    others = set()
    while len(others) < 4:
        word = vocab[random.choice(keys)]
        if word != answer:
            others.add(word)
    others.add(answer)
    print(f"Co to znaczy '{key}' po Polsku???\n")
    letters = "ABCDE"
    mc = {k:v for (k,v) in zip(letters, others)}
    for k,v in mc.items():
        print(f"{k}: {v}")
    response = input("\n> ")
    try:
        while mc.get(response.upper()) != answer:
            response = input("Nie całkowice...\n> ")
        else:
            praise(zacheta)
    except:
        print("You entered invalid input! Enter A, B, C, D, or E!")

#####################################################################

def type_in_questions(vocab, number=15):
    keys = [random.choice(list(vocab.keys())) for i in range(number)]
    for key in keys[:8]:
        print(f"Co to znaczy '{key}' po polsku?")
        response = input()
        while response != vocab[key]:
            print(vocab[key], "\n\n")
            response = input()
        praise(zacheta)

#####################################################################

for i in range(25):
    multiple_choice(brand_new_vocab)
type_in_questions(brand_new_vocab, number=5)

for i in range(15):
    multiple_choice(new_vocab)
type_in_questions(new_vocab, number=5)

for i in range(25):
    multiple_choice(vocab)
type_in_questions(vocab)


 
