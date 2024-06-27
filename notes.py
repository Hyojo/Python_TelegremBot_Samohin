import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from secrets import API_TOKEN


def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w+") as notes_file:
            notes_file.write(note_text)

        return print(f"\nNote {note_name} has been built successfully.")

    except OSError:
        print(f"\nName {note_name} invalid file name.")


def create_note(note_text, note_name):
    build_note(note_text, note_name)


def read_note(note_name):
    try:
        with open(f"{note_name}.txt", "r") as notes_file:
            notes_text = notes_file.read()
        return notes_text

    except FileNotFoundError:
        print("Note not found")


def edit_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "r") as notes_file:
            notes_text = notes_file.read()
            print(notes_text)

        with open(f"{note_name}.txt", "w") as notes_file:
            notes_file.write(note_text)

    except FileNotFoundError:
        print("Note not found")

    except IOError:
        print(f"\nName {note_name} invalid file.")


def delete_note(note_name):
    try:
        os.remove(f"{note_name}.txt")

    except FileNotFoundError:
        print("File not found")

    except OSError:
        print(f"\nName {note_name} failed to delete.")


def display_notes():
    notes = [x for x in os.listdir() if x.endswith(".txt")]
    all_text = []

    for note in notes:
        with open(note, "r") as notes_file:
            all_text.append(notes_file.read())

    all_text.sort(key=len, reverse=True)

    return all_text


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

        # match choice:
        #     case "1":
        #         create_note()
        #     case "2":
        #         read_note()
        #     case "3":
        #         edit_note()
        #     case "4":
        #         delete_note()
        #     case "5":
        #         display_notes()
        #     case "6":
        #         start = False


updater = Updater(token=API_TOKEN)


def create_note_handler(update, context):
    try:
        note_text = update.message.text
        note_name = update.message.chat_id
        create_note(note_text, note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def read_note_handler(update, context):
    try:
        note_name = update.message.text
        text = read_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name}:\n{text}")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def update_note_handler(update, context):
    try:
        note_text = update.message.text
        note_name = update.message.chat_id
        edit_note(note_text, note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} обновлена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def delete_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        delete_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


def display_note_handler(update, context):
    try:
        text = display_notes()
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметкb:\n{text}.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


updater.dispatcher.add_handler(CommandHandler("create", create_note_handler))
updater.dispatcher.add_handler(CommandHandler("read", read_note_handler))
updater.dispatcher.add_handler(CommandHandler("update", edit_note))
updater.dispatcher.add_handler(CommandHandler("delete", delete_note_handler))
updater.dispatcher.add_handler(CommandHandler("showAll", display_note_handler))

updater.start_polling()

#pip install urllib3==1.26.15 - без нее не работает, а на сайте не сказано