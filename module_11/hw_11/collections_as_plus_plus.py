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
            return days_left, next_birthday
        return None, None

    def __str__(self):
        return f"Name: {self.name}\nPhones: {', '.join(str(phone) for phone in self.phones)}"

    def __repr__(self):
        return f"Record(name={self.name}, phones={self.phones})"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, identifier):
        if isinstance(identifier, str):
            if identifier in self.data:
                del self.data[identifier]
            else:
                raise KeyError(f"No record found with name '{identifier}'")
        elif isinstance(identifier, int):
            if 0 <= identifier < len(self.data):
                del self.data[list(self.data.keys())[identifier]]
            else:
                raise IndexError(f"Index '{identifier}' is out of range")
        else:
            raise TypeError("Invalid identifier type. Expected str or int.")

    def search(self, keyword):
        results = []
        for record in self.data.values():
            if keyword.lower() in record.name.value.lower():
                results.append(record)
            else:
                for phone in record.phones:
                    if keyword in phone.value:
                        results.append(record)
                        break
        return results

    def __str__(self):
        return "\n\n".join(str(record) for record in self.data.values())

    def __repr__(self):
        return repr(self.data)

    def iterator(self, page_size):
        if page_size <= 0:
            raise ValueError("Page size must be a positive integer.")
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

        page_records = self.records[self.current_index: self.current_index + self.page_size]
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

# Search for records by keyword
keyword = "ev"
search_results = address_book.search(keyword)
print(f"\nSearch results for keyword '{keyword}':")
for record in search_results:
    print(record)

# Remove a record by name
# record_name = "Yevhen Hrebonkin"
# address_book.remove_record(record_name)

# # Print all records after removal
# print("\nAddress book after record removal:")
# print(address_book)

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

# Print days to next birthday
for record in address_book.data.values():
    days_left, next_birthday = record.days_to_birthday()
    if days_left is not None:
        print(f"\nNext birthday for {record.name.value}: {next_birthday}. Days left: {days_left}")
    else:
        print(f"\nNo birthday set for {record.name.value}")
