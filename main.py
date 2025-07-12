# Bot-Helper
## 📖 Опис
# Цей проєкт є персональним помічником,
# який допомагає користувачам зберігати контакти та нотатки.

# - Team_Lead: [Ім’я]
# - Dev 1: [Ім’я]
# - Dev 2: [Ім’я]
# - Dev 3: [Ім’я]
# - Scrum Master: [Ім’я]

## 📁 Сервіси
# - contact_book.py
# - note_book.py
# - storage.py
# - validators.py

## 📁 Структура проєкту


#----

## ✅ Ліцензія

# MIT License
#----

from services.contact_book import ContactBook
from services.note_book import NoteBook
from services.storage import save_data, load_data
from utils.validators import validate_email, validate_phone
from utils.parsers import suggest_command  # <-- з "s"




def main():
    print("👋 Вітаємо у Персональному Помічнику!")
    contact_book, note_book = load_data()

    while True:
        command = input("\nВведіть команду (help - список команд): ").strip().lower()

        if command == "help":
            print("""
📋 Доступні команди:
    add contact        - Додати контакт
    show birthdays     - Показати дні народження
    find contact       - Знайти контакт
    edit contact       - Редагувати контакт
    delete contact     - Видалити контакт

    add note           - Додати нотатку
    find note          - Знайти нотатку
    edit note          - Редагувати нотатку
    delete note        - Видалити нотатку

    save               - Зберегти дані
    exit               - Вийти з програми
            """)
        
        elif command == "add contact":
            name = input("Ім’я: ")
            phone = input("Телефон: ")
            if not validate_phone(phone):
                print("❌ Некоректний номер телефону!")
                continue
            email = input("Email: ")
            if not validate_email(email):
                print("❌ Некоректна електронна пошта!")
                continue
            address = input("Адреса: ")
            birthday = input("Дата народження (рррр-мм-дд): ")
            contact_book.add_contact(name, phone, email, address, birthday)
            print("✅ Контакт додано.")

        elif command == "add note":
            text = input("Введіть нотатку: ")
            note_book.add_note(text)
            print("📝 Нотатку збережено.")

        elif command == "save":
            save_data(contact_book, note_book)
            print("💾 Дані збережено.")

        elif command == "exit":
            save_data(contact_book, note_book)
            print("👋 До побачення!")
            break

        else:
            suggestion = suggest_command(command)
        if  suggestion:
            print(f"🤖 Невідома команда. Можливо ви мали на увазі: `{suggestion}`?")
        else:
            print("❌ Невідома команда. Введіть `help` для перегляду списку.")

if __name__ == "__main__":
    main()