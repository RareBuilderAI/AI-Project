import json


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = load_notes()


def add_note():
    title = input("\nNote title: ")
    content = input("Write your note: ")

    note = {
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes()

    print("✅ Note saved:", title)


def view_notes():
    print("\nYour notes:")

    if not notes:
        print("No notes yet.")
        return

    for index, note in enumerate(notes, start=1):
        print("\nNote", index)
        print("Title:", note["title"])
        print("Content:", note["content"])


def search_notes():
    search = input("\nSearch for a note: ").lower()

    found = False

    for note in notes:
        if search in note["title"].lower() or search in note["content"].lower():
            print("\nFound:")
            print("Title:", note["title"])
            print("Content:", note["content"])
            found = True

    if not found:
        print("❌ No note found.")


def delete_note():
    view_notes()

    if not notes:
        return

    choice = input("\nEnter the number of the note to delete: ")

    if choice.isdigit():
        note_number = int(choice)

        if 1 <= note_number <= len(notes):
            removed_note = notes.pop(note_number - 1)

            save_notes()

            print("🗑️ Deleted:", removed_note["title"])


print("📝 Notes App")


while True:

    print("\nWhat would you like to do?")

    print("1. Add note")
    print("2. View notes")
    print("3. Search notes")
    print("4. Delete note")
    print("5. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_notes()

    elif choice == "4":
        delete_note()

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Please choose 1-5.")
