contacts = {}

while True:
    print("\nContact Book 📒")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved! ✅")

    elif choice == "2":
        print("\nSaved Contacts:")

        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        search_name = input("Enter name to search: ")

        if search_name in contacts:
            print("Phone number:", contacts[search_name])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Contact Book closed 👋")
        break

    else:
        print("Invalid option")
