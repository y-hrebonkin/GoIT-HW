class Field:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def set_value(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def __str__(self):
        phones = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phones}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, index):
        if 0 <= index < len(self.phones):
            del self.phones[index]
    
    def edit_phone(self, index, phone):
        if 0 <= index < len(self.phones):
            self.phones[index].set_value(phone)


class AddressBook(dict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def remove_record(self, name):
        del self.data[name]
    
    def search_records(self, criteria):
        results = []
        for record in self.data.values():
            if criteria.lower() in record.name.value.lower():
                results.append(record)
            for phone in record.phones:
                if criteria in phone.value:
                    results.append(record)
        return results


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid command! Please try again."
        except ValueError:
            return "Invalid input! Please try again."
        except IndexError:
            return "Invalid command! Please try again."
    return inner


@input_error
def hello_command():
    return "How can I help you?"


@input_error
def create_contact_command(name, phone, address_book):
    if name in address_book:
        return f"Contact '{name}' already exists. Use 'change' command to update the phone number."
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return f"Contact '{name}' with phone number '{phone}' created."


@input_error
def change_contact_command(name, phone, address_book):
    if name not in address_book:
        return f"Contact '{name}' does not exist. Use 'add' command to create a new contact."
    record = address_book[name]
    record.add_phone(phone)
    return f"Phone number for contact '{name}' changed to '{phone}'."


@input_error
def get_phone_command(name, address_book):
    if name not in address_book:
        return f"Contact '{name}' does not exist."
    record = address_book[name]
    return f"The phone number(s) for contact '{name}' is/are: {', '.join(str(phone) for phone in record.phones)}"


def show_all_contacts_command(address_book):
    if len(address_book) == 0:
        return "No contacts found."
    else:
        output = "Contacts:\n"
        for record in address_book.values():
            output += str(record) + "\n"
        return output.strip()


def main():
    address_book = AddressBook()
    
    while True:
        command = input("Enter a command: ").lower()

        if command.startswith("add"):
            _, name, phone = command.split()
            record = Record(name)
            record.add_phone(phone)
            address_book.add_record(record)
            response = f"Contact '{name}' with phone number '{phone}' created."
        elif command.startswith("change"):
            _, name, phone = command.split()
            if name in address_book:
                record = address_book[name]
                record.edit_phone(record.phones[0].value, phone)
                response = f"Phone number for contact '{name}' changed to '{phone}'."
            else:
                response = f"Contact '{name}' does not exist. Use 'add' command to create a new contact."
        elif command.startswith("phone"):
            _, name = command.split()
            if name in address_book:
                record = address_book[name]
                phone = record.phones[0].value
                response = f"The phone number for contact '{name}' is '{phone}'."
            else:
                response = f"Contact '{name}' does not exist."
        elif command == "show all":
            response = show_all_contacts_command(address_book)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            response = "Invalid command! Please try again."

        print(response)


def show_all_contacts_command(address_book):
    if len(address_book) == 0:
        return "No contacts found."
    else:
        output = "Contacts:\n"
        for name, record in address_book.items():
            phones = ", ".join([phone.value for phone in record.phones])
            output += f"{name}: {phones}\n"
        return output.strip()


# Run the bot
main()