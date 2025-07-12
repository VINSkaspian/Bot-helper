import pickle
import os

DATA_DIR = "data"
CONTACT_FILE = os.path.join(DATA_DIR, "contacts.bin")
NOTE_FILE = os.path.join(DATA_DIR, "notes.bin")

def save_data(contact_book, note_book):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(CONTACT_FILE, "wb") as f:
        pickle.dump(contact_book, f)
    with open(NOTE_FILE, "wb") as f:
        pickle.dump(note_book, f)

def load_data():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "rb") as f:
            contact_book = pickle.load(f)
    else:
        from services.contact_book import ContactBook
        contact_book = ContactBook()

    if os.path.exists(NOTE_FILE):
        with open(NOTE_FILE, "rb") as f:
            note_book = pickle.load(f)
    else:
        from services.note_book import NoteBook
        note_book = NoteBook()

    return contact_book, note_book
