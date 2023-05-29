class Field:
    def __init__(self, value=None):
        self.value = value


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

    def match(self, criteria):
        if criteria.lower() in self.name.value.lower():
            return True
        for phone in self.phones:
            if criteria in phone.value:
                return True
        return False


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
