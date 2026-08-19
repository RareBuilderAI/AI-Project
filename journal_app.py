print("Journal App 📓")

print("1. Write Note")
print("2. Read Notes")

choice = input("Choose an option: ")

if choice == "1":
    note = input("Write your note: ")

    file = open("journal.txt", "a")

    file.write(note + "\n")

    file.close()

    print("Note saved! ✅")

elif choice == "2":
    file = open("journal.txt", "r")

    notes = file.read()

    file.close()

    print("\nYour Notes:")
    print(notes)

else:
    print("Invalid option")