from datetime import datetime

class Field:
    def __init__(self, value=None):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise ValueError("Field value cannot be None")
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value=None):
        if value is None:
            raise ValueError("Phone number cannot be None")
        super().__init__(value)
        self._validate_phone_number()

    def _validate_phone_number(self):
        if not self._is_valid_phone_number():
            raise ValueError("Invalid phone number format")

    def _is_valid_phone_number(self):
        # Add your phone number validation logic here
        # Example: Check if the phone number has 10 digits
        return len(str(self.value)) == 10


class Birthday(Field):
    def __init__(self, value=None):
        if value is None:
            raise ValueError("Birthday cannot be None")
        super().__init__(value)
        self._validate_birthday()

    def _validate_birthday(self):
        if not self._is_valid_birthday():
            raise ValueError("Invalid birthday format")

    def _is_valid_birthday(self):
        today = datetime.today().date()
        return self.value.date() < today


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

    def match(self, criteria):
        if criteria.lower() in self.name.value.lower():
            return True
        for phone in self.phones:
            if criteria in phone.value:
                return True
        return False

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today().date()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
            return (next_birthday - today).days
        return None


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record

    def search_records(self, criteria):
        results = []
        for record in self.data.values():
            if record.match(criteria):
                results.append(record)
        return results

    def iterator(self, n):
        records = list(self.data.values())
        total_records = len(records)
        num_pages = (total_records - 1) // n + 1
        for page in range(num_pages):
            start_idx = page * n
            end_idx = (page + 1) * n
            yield records[start_idx:end_idx]


# Приклад використання

# Створення адресної книги
address_book = AddressBook()

# Створення записів
record1 = Record("John Doe", birthday=datetime(1990, 5, 15))
record1.add_phone("1234567890")
record1.add_phone("9876543210")

record2 = Record("Jane Smith", birthday=datetime(1985, 9, 20))
record2.add_phone("1112223333")

# Додавання записів до адресної книги
address_book.add_record(record1)
address_book.add_record(record2)

# Пошук записів за критерієм
results = address_book.search_records("John")
for result in results:
    print(result.name.value)

# Перевірка кількості днів до дня народження
days = record1.days_to_birthday()
if days is not None:
    print(f"Days to birthday: {days}")
else:
    print("No birthday specified")

# Пагінація записів
for page_records in address_book.iterator(1):
    for record in page_records:
        print(record.name.value)
    print("-----")
