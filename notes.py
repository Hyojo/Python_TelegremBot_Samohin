import json
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
        print("6. Create a new Note")
        print("7. Read Note")
        print("8. Edit Note")
        print("9. Delete Note")
        print("10. Display Notes")
        print("11. Exit\n")

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


class Calendar:
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, event_time, event_details):
        event_id = str(len(self.events) + 1)
        event = {
            'id': event_id,
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'details': event_details
        }
        self.events[event_id] = event
        return event_id

    def read_event(self, event_id):
        event = self.events[event_id]
        return event

    def edit_event(self, event_id, event_name, event_date, event_time, event_details):
        event = {
            'id': event_id,
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'details': event_details
        }
        self.events[event_id] = event
        return event_id

    def delete_event(self, event_id):
        self.events.pop(event_id)
        return event_id

    def show_events(self):
        return self.events


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


calendar = Calendar()


def event_create_handler(update, context):
    try:
        event_name = update.message.text[14:]
        event_date = "2023-03-14"
        event_time = "14:00"
        event_details = "Описание события"

        event_id = calendar.create_event(event_name, event_date, event_time, event_details)

        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Событие {event_name} создано и имеет номер {event_id}.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


def event_read_handler(update, context):
    try:
        event_id = update.message.text[12:]

        event = calendar.read_event(event_id)

        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"{event}")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


def event_edit_handler(update, context):
    try:
        event_id = update.message.text[12:]
        event_name = calendar.events[event_id]['name']
        event_date = "2023-03-14"
        event_time = "14:00"
        event_details = "Описание события изменено"

        event_id = calendar.edit_event(event_id, event_name, event_date, event_time, event_details)

        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Событие {event_name} изменено и имеет номер {event_id}.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


def event_delete_handler(update, context):
    try:
        event_id = update.message.text[14:]

        event_name = calendar.events[event_id]['name']
        event_id = calendar.delete_event(event_id)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Событие {event_name} удалено под номером {event_id}.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


def event_all_handler(update, context):
    try:

        events =  json.dumps(calendar.show_events(), indent=4, sort_keys=True, default=str, )

        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"{events}")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


updater.dispatcher.add_handler(CommandHandler("create", create_note_handler))
updater.dispatcher.add_handler(CommandHandler("read", read_note_handler))
updater.dispatcher.add_handler(CommandHandler("update", edit_note))
updater.dispatcher.add_handler(CommandHandler("delete", delete_note_handler))
updater.dispatcher.add_handler(CommandHandler("showAll", display_note_handler))

updater.dispatcher.add_handler(CommandHandler('create_event', event_create_handler))
updater.dispatcher.add_handler(CommandHandler('read_event', event_read_handler))
updater.dispatcher.add_handler(CommandHandler('edit_event', event_edit_handler))
updater.dispatcher.add_handler(CommandHandler('delete_event', event_delete_handler))
updater.dispatcher.add_handler(CommandHandler('show_events', event_all_handler))

updater.start_polling()

# pip install urllib3==1.26.15 - без нее не работает, а на сайте не сказано
