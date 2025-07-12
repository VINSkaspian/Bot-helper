import os
from services.contact_book import ContactBook
from services.note_book import NoteBook
from services.storage import save_data, load_data, DATA_DIR

def test_save_and_load_data(tmp_path):
    contact_book = ContactBook()
    contact_book.add_contact("Тест", "+380111111111", "test@test.com", "Test address", "2000-01-01")
    
    note_book = NoteBook()
    note_book.add_note("Це збережена нотатка", ["зберігання"])

    # Зміна DATA_DIR тимчасово
    orig_data_dir = DATA_DIR
    test_dir = tmp_path / "data"
    os.makedirs(test_dir, exist_ok=True)
    from services import storage
    storage.DATA_DIR = str(test_dir)

    save_data(contact_book, note_book)
    loaded_contact_book, loaded_note_book = load_data()

    assert len(loaded_contact_book.contacts) == 1
    assert len(loaded_note_book.notes) == 1
    assert loaded_note_book.notes[0].tags == ["зберігання"]

    # Повернути DATA_DIR назад
    storage.DATA_DIR = orig_data_dir
