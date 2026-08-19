import json


def save_passwords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)


def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


passwords = load_passwords()


def add_password():
    website = input("\nWebsite name: ")
    username = input("Username: ")
    password = input("Password: ")

    password_item = {
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(password_item)

    save_passwords()

    print("✅ Password saved:", website)


def view_passwords():
    print("\nYour passwords:")

    if not passwords:
        print("No passwords saved.")
        return

    for index, item in enumerate(passwords, start=1):
        print("\nPassword", index)
        print("Website:", item["website"])
        print("Username:", item["username"])
        print("Password:", item["password"])


def search_password():
    search = input("\nSearch website: ").lower()

    found = False

    for item in passwords:
        if search in item["website"].lower():

            print("\nFound:")
            print("Website:", item["website"])
            print("Username:", item["username"])
            print("Password:", item["password"])

            found = True

    if not found:
        print("❌ No password found.")


def delete_password():
    view_passwords()

    if not passwords:
        return

    choice = input("\nEnter the number of password to delete: ")

    if choice.isdigit():

        password_number = int(choice)

        if 1 <= password_number <= len(passwords):

            removed = passwords.pop(password_number - 1)

            save_passwords()

            print("🗑️ Deleted:", removed["website"])


print("🔐 Password Manager")


while True:

    print("\nWhat would you like to do?")

    print("1. Add password")
    print("2. View passwords")
    print("3. Search password")
    print("4. Delete password")
    print("5. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Please choose 1-5.")