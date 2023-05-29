from collections import UserDict
from datetime import date
from collections.abc import Iterator

class Field:
    def __init__(self, value=None):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value=None):
        super().__init__()
        self.value = value

    @Field.value.setter
    def value(self, value):
        if value is None or self.validate_phone(value):
            self._Field__value = value
        else:
            raise ValueError("Invalid phone number format")

    @staticmethod
    def validate_phone(phone):
        # Add your phone number validation logic here
        # Return True if the phone number is valid, False otherwise
        return True  # Placeholder implementation

class Birthday(Field):
    def __init__(self, value=None):
        super().__init__()
        self.value = value

    @Field.value.setter
    def value(self, value):
        if value is None or self.validate_birthday(value):
            self._Field__value = value
        else:
            raise ValueError("Invalid birthday format")

    @staticmethod
    def validate_birthday(birthday):
        # Add your birthday validation logic here
        # Return True if the birthday is valid, False otherwise
        return True  # Placeholder implementation

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def days_to_birthday(self):
        if self.birthday.value:
            today = date.today()
            current_year_birthday = date(today.year, self.birthday.value.month, self.birthday.value.day)
            if current_year_birthday >= today:
                next_birthday = current_year_birthday
            else:
                next_birthday = date(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            days_left = (next_birthday - today).days
            return days_left
        return None

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

    def iterator(self, page_size):
        return AddressBookIterator(self, page_size)

class AddressBookIterator(Iterator):
    def __init__(self, address_book, page_size):
        self.address_book = address_book
        self.page_size = page_size
        self.records = list(address_book.data.values())
        self.current_index = 0

    def __next__(self):
        if self.current_index >= len(self.records):
            raise StopIteration

        page_records = self.records[self.current_index : self.current_index + self.page_size]
        self.current_index += self.page_size
        return "\n\n".join(str(record) for record in page_records)

address_book = AddressBook()

record1 = Record("Yevhen Hrebonkin", birthday=date(1987, 1, 23))
record1.add_phone("0666666114")
record1.add_phone("0730876937")

record2 = Record("Yurii Haharin", birthday=date(1985, 8, 20))
record2.add_phone("0675555555")

address_book.add_record(record1)
address_book.add_record(record2)

# Print all records
print(address_book)

# Print records using pagination
page_size = 1
address_book_iterator = address_book.iterator(page_size)
while True:
    try:
        page = next(address_book_iterator)
        print("\n--- Page ---")
        print(page)
    except StopIteration:
        break
