from collections import UserDict
from address_book.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise ValueError("Record with this name already exists.")
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())