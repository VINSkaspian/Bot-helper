from models.contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address, birthday):
        contact = Contact(name, phone, email, address, birthday)
        self.contacts.append(contact)

    def find_contact(self, keyword):
        return [c for c in self.contacts if keyword.lower() in c.name.lower()]

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]

    def edit_contact(self, name, **kwargs):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = kwargs.get("phone", contact.phone)
                contact.email = kwargs.get("email", contact.email)
                contact.address = kwargs.get("address", contact.address)
                contact.birthday = kwargs.get("birthday", contact.birthday)

    def get_upcoming_birthdays(self, days_ahead):
        from datetime import datetime, timedelta
        today = datetime.today().date()
        upcoming = []
        for contact in self.contacts:
            if contact.birthday:
                try:
                    bday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
                    bday_this_year = bday.replace(year=today.year)
                    if today <= bday_this_year <= today + timedelta(days=days_ahead):
                        upcoming.append(contact)
                except ValueError:
                    continue
        return upcoming
