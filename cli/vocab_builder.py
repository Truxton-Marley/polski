import random
from slowa_vocab_builder import vocab, new_vocab



#####################################################################


print(vocab)
print()

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
            print("Dobrze!!!\n")
    except:
        print("You entered invalid input! Enter A, B, C, D, or E!")

#####################################################################

for i in range(15):
    multiple_choice(new_vocab)
    #multiple_choice(new_vocab, new_all_keys)

for i in range(25):
    multiple_choice(vocab)
    #multiple_choice(vocab, all_keys)

# Type in response:
keys = [random.choice(list(vocab.keys())) for i in range(18)]
for key in keys[:8]:
    print(f"Co to znaczy '{key}' po polsku?")
    response = input()
    while response != vocab[key]:
        print(vocab[key], "\n\n")
        response = input()
    print("\nDobrze!\n")

 
