import random
import string


print("🔐 Password Generator")
print("Type 'quit' to exit.")


while True:

    length_input = input(
        "\nHow many characters do you want? "
    )

    if length_input.lower() == "quit":
        print("Password Generator closed.")
        break

    try:
        length = int(length_input)

    except ValueError:
        print("Please enter a valid number.")
        continue

    if length < 4:
        print("Password length must be at least 4 characters.")
        continue

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*"

    characters = letters + numbers + symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your password is:", password)
