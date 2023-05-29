from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def __str__(self):
        return f"Name: {self.name}\nPhones: {', '.join(str(phone) for phone in self.phones)}"

    def __repr__(self):
        return f"Record(name={self.name}, phones={self.phones})"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return "\n\n".join(str(record) for record in self.data.values())

    def __repr__(self):
        return repr(self.data)


address_book = AddressBook()

record1 = Record("Yevhen Hrebonkin")
record1.add_phone("0666666114")
record1.add_phone("0730876937")

record2 = Record("Yurii Haharin")
record2.add_phone("0675555555")

address_book.add_record(record1)
address_book.add_record(record2)

print(address_book)
