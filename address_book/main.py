from address_book.address_book import AddressBook
from address_book.record import Record


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Додавання записів
    john_record = Record("John")
    john_record.add_phone("1234567890")
    book.add_record(john_record)

    print(book)

if __name__ == "__main__":
    main()
