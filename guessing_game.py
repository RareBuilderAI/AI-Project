import random


print("🎯 Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")
print("Type 'quit' to exit.")


while True:

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:

        guess = input("\nEnter your guess: ")

        if guess.lower() == "quit":
            print("Game closed.")
            exit()

        try:
            guess = int(guess)

        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("🎉 Correct!")
            print("You guessed the number in", attempts, "attempts.")
            break

    play_again = input(
        "\nDo you want to play again? (yes/no): "
    )

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
