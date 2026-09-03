contacts = {}


while True:

    print("\n📒 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()

        if not name or not phone:
            print("Name and phone number are required.")
            continue

        contacts[name] = phone

        print("Contact saved! ✅")

    elif choice == "2":

        print("\nSaved Contacts:")

        if not contacts:
            print("No contacts saved yet.")

        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":

        search_name = input(
            "Enter name to search: "
        ).strip()

        if search_name in contacts:
            print(
                "Phone number:",
                contacts[search_name]
            )

        else:
            print("Contact not found.")

    elif choice == "4":

        print("Contact Book closed 👋")
        break

    else:

        print("Invalid option.")
