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

   # Редагування телефону для John
    try:
        john = book.find("John")
        print("\nПеред редагуванням у записі John:", john)  # Діагностика
        john.edit_phone("1234567890", "1112223333")
        print("\nПісля редагування номера у записі John:")
        print(john)  # Виведення запису John
    except ValueError as e:
        print(f"Error while editing phone: {e}")

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"\nПошук телефону: {john.name.value} має номер {found_phone.value}.")
    else:
        print("\nТелефон не знайдено.")

    # === Видалення запису ===
    try:
        book.delete("Jane")
        print("\nПісля видалення запису Jane:")
        print(book)  # Виведення адресної книги після видалення
    except ValueError as e:
        print(f"Error while deleting record: {e}")


if __name__ == "__main__":
    main()
