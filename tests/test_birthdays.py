from datetime import datetime, timedelta
from services.contact_book import ContactBook

def test_get_upcoming_birthdays():
    book = ContactBook()
    today = datetime.today()
    upcoming_day = (today + timedelta(days=5)).strftime("%Y-%m-%d")
    
    book.add_contact("Тест", "+380123123123", "test@email.com", "Kyiv", upcoming_day)
    result = book.get_upcoming_birthdays(7)
    
    assert len(result) == 1
    assert result[0].name == "Тест"
