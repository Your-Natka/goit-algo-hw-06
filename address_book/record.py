from address_book.fields import Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
    # Перевірка валідності нового номера
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone number must contain exactly 10 digits.")

        # Видалення старого номера, якщо знайдено
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.add_phone(new_phone)
                return
    
        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"
