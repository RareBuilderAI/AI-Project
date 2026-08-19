import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct! You guessed the number 🎉")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")