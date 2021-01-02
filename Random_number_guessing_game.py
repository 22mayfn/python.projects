import random

random_number = random.randint(0, 100)


init_score = 3

while True:
    a = input("Guess a number between 0 and 100: ")
    a = int(a)
    if a == random_number:
        print("You guessing correctly!")
        break
    try:
        a = int(a)
    except ValueError:
        print("Incorrect. Please try again.")
        init_score -= 1
        print("Score: ", init_score)
