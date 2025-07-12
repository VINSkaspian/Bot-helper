import pytest
from services.note_book import NoteBook

@pytest.fixture
def notebook():
    return NoteBook()

def test_add_note(notebook):
    notebook.add_note("Це тестова нотатка", ["тест"])
    assert len(notebook.notes) == 1
    assert "тест" in notebook.notes[0].tags
