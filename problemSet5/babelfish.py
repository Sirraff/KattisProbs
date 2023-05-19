translation = {}

# Read dict
while True:
    try:
        entry = input()
        if entry == "":
            break
        english, foreign = entry.split()
        translation[foreign] = english
    except EOFError:  # stop the program if there are no more inputs
        break

while True:
    try:
        word = input()
        print(translation.get(word, "eh"))
    except EOFError:  # same as above
        break
