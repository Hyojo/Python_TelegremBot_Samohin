import os


def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w+") as notes_file:
        notes_file.write(note_text)

    return print(f"\nNote {note_name} has been built successfully.")


def create_note():
    note_name = input("Enter a note name: ")
    note_text = input("Enter a note text: ")
    build_note(note_text, note_name)


def read_note():
    note_name = input("Enter a note name: ")

    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", "r") as notes_file:
            notes_text = notes_file.read()
        return notes_text

    print("Note not found")


def edit_note():
    note_name = input("Enter a note name: ")

    if not os.path.isfile(f"{note_name}.txt"):
        return print("Note not found")

    with open(f"{note_name}.txt", "r") as notes_file:
        notes_text = notes_file.read()
        print(notes_text)

    with open(f"{note_name}.txt", "w") as notes_file:
        new_text = input("Enter a note text: ")
        notes_file.write(new_text)


def delete_note():
    note_name = input("Enter a note name: ")

    if os.path.isfile(f"{note_name}.txt"):
        os.remove(f"{note_name}.txt")


def main():
    print("\nWelcome to Notes Bot")

    start = True

    while start:
        print("\nStart menu:")
        print("1. Create a new Note")
        print("2. Read Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                create_note()
            case "2":
                text = read_note()
                print(f"Text:\n {text}")
            case "3":
                edit_note()
            case "4":
                delete_note()
            case "5":
                start = False


main()
