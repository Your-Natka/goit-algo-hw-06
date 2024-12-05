from address_book.address_book import AddressBook
from address_book.record import Record


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Додавання записів
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Створення запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення поточної адресної книги
    print("Адресна книга після додавання записів:")
    print(book)

   # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print("\nПісля редагування номера у записі John:")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"\n{john.name.value}: {found_phone.value}")  # Виведення: John: 5555555555
    else:
        print("\nТелефон 5555555555 не знайдено у записі John.")
    # Видалення запису Jane
    try:
        book.delete("Jane")
        print("\nЗапис Jane успішно видалено.")
        print("Поточна адресна книга після видалення:")
        print(book)
    except ValueError as e:
        print(f"Помилка під час видалення запису Jane: {e}")


if __name__ == "__main__":
    main()
