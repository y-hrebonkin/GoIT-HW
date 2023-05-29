import json
import re
from datetime import datetime

class Field:
    def __init__(self, value=None):
        self.__value = None
        self.value = value

    def validate(self, value):
        return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.validate(new_value):
            self.__value = new_value
        else:
            raise ValueError("Invalid field value")

    def to_dict(self):
        return self.value

class Phone(Field):
    def validate(self, value):
        if value is not None and not isinstance(value, str):
            return False

        if value is not None:
            pattern = r'^\+\d{1,3}\d{9}$'
            if not re.match(pattern, value):
                return False

        return True

class Birthday(Field):
    def validate(self, value):
        if value is not None and not isinstance(value, str):
            return False

        if value is not None:
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                return False

        return True

class Record:
    def __init__(self, name, birthday=None):
        self.name = Field()
        self.birthday = Birthday()
        self.phones = []

        self.name.value = name
        self.birthday.value = birthday

    def add_phone(self, phone):
        phone_field = Phone(phone)
        self.phones.append(phone_field)

    def to_dict(self):
        return {
            "name": self.name.to_dict(),
            "birthday": self.birthday.to_dict(),
            "phones": [phone.to_dict() for phone in self.phones]
        }

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_record(self, record):
        self.contacts.append(record)

    def remove_record(self, name):
        for record in self.contacts:
            if record.name.value == name:
                self.contacts.remove(record)
                break

    def save_to_file(self, filename):
        data = [record.to_dict() for record in self.contacts]
        with open(filename, "w") as file:
            json.dump(data, file, default=lambda x: x.__dict__, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.contacts = []
            for record_data in data:
                record = Record(record_data['name'], record_data['birthday'])
                for phone in record_data['phones']:
                    record.add_phone(phone)
                self.add_record(record)

    def search(self, query):
        results = []
        for record in self.contacts:
            if query.lower() in record.name.value.lower():
                results.append(record)
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
                    break
        return results

    def days_to_birthday(self, name):
        for record in self.contacts:
            if record.name.value == name:
                birthday = record.birthday.value
                if birthday:
                    today = datetime.today()
                    next_birthday = datetime.strptime(birthday, "%Y-%m-%d").replace(year=today.year)
                    if today > next_birthday:
                        next_birthday = next_birthday.replace(year=today.year + 1)
                    days_left = (next_birthday - today).days
                    return days_left
        return None

# Example usage
address_book = AddressBook()

record1 = Record("Yevhen Hrebonkin", "1987-01-23")
record1.add_phone("+380730876937")

address_book.add_record(record1)
address_book.save_to_file("address_book.json")

new_address_book = AddressBook()
new_address_book.load_from_file("address_book.json")

results = new_address_book.search("Yevhen")
for record in results:
    print(record.name.value, [phone.value for phone in record.phones])

days_left = new_address_book.days_to_birthday("Yevhen Hrebonkin")
print("Days left to birthday:", days_left)
