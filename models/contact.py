class Contact:
    def __init__(self, name, phone, email, address="", birthday=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday

    def __str__(self):
        return f"{self.name} | 📞 {self.phone} | ✉️ {self.email} | 🏠 {self.address} | 🎂 {self.birthday}"
