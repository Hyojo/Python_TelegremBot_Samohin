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
        return print(notes_text)

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


def display_sorted_notes():
    notes = [x for x in os.listdir() if x.endswith(".txt")]
    all_text = []

    for note in notes:
        with open(note, "r") as notes_file:
            all_text.append(notes_file.read())

    all_text.sort(key=lambda x: len(x), reverse=True)

    for text in all_text:
        print(text)


def main():
    print("\nWelcome to Notes Bot")

    start = True

    while start:
        print("\nStart menu:")
        print("1. Create a new Note")
        print("2. Read Note")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Display Notes")
        print("6. Exit\n")

        choice = input("Enter your choice: ")
        print("\n")

        match choice:
            case "1":
                create_note()
            case "2":
                read_note()
            case "3":
                edit_note()
            case "4":
                delete_note()
            case "5":
                display_sorted_notes()
            case "6":
                start = False


main()
