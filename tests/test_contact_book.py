import pytest
from services.contact_book import ContactBook

@pytest.fixture
def book():
    return ContactBook()

def test_add_contact(book):
    book.add_contact("Іван", "+380123456789", "ivan@example.com", "Київ", "2000-01-01")
    assert len(book.contacts) == 1
    assert book.contacts[0].name == "Іван"

def test_find_contact(book):
    book.add_contact("Марія", "+380987654321", "maria@example.com", "", "")
    results = book.find_contact("Мар")
    assert len(results) == 1
    assert results[0].email == "maria@example.com"
