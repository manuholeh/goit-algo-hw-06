from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(str(value))

class Phone(Field):
    def __init__(self, value):
        value_str = str(value)
        if len(value_str) != 10 or not value_str.isdigit():
            raise ValueError("Перевірте правильність введення номеру")
        super().__init__(value_str)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)
        else:
            raise ValueError("Номер не знайдено")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) and Phone(new_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Перевірте правильність даних")

    def find_phone(self, phone):
        found = [p for p in self.phones if p.value == phone]
        if found:
            return found[0]
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"





class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name,None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        result = []
        for record in self.data.values():
            phones = '; '.join(p.value for p in record.phones)
            result.append(f"Contact name: {record.name.value}, phones: {phones}")
        return '\n'.join(result)



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
#john_record.remove_phone("123456789")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)
print("-----")

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1111111111")
print(book)

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
print("-----")
# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
print("-----")
# Видалення запису Jane
book.delete("Jane")
print(book.find("Jane"))

