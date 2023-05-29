from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __set__(self, instance, value):
        if not value.isdigit():
            raise ValueError("Phone number can only contain digits.")
        self.value = value


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def __str__(self):
        phones = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}\nPhone(s): {phones}"


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return inner


@input_error
def command_parser(command):
    command = command.lower().strip()
    if command.startswith("add"):
        return "add", command[4:].strip()
    elif command.startswith("change"):
        return "change", command[7:].strip()
    elif command.startswith("phone"):
        return "phone", command[6:].strip()
    elif command == "show all":
        return "show all", ""
    elif command in ["good bye", "close", "exit"]:
        return "exit", ""
    else:
        return "", ""


@input_error
def handle_add(address_book, args):
    name, phone = args.split(" ")
    record = Record(Name(name))
    record.add_phone(Phone(phone))
    address_book.add_record(record)
    return "Contact added successfully."


@input_error
def handle_change(address_book, args):
    name, phone = args.split(" ")
    record = address_book.data[name]
    record.edit_phone(record.phones[0], Phone(phone))
    return "Phone number changed successfully."


@input_error
def handle_phone(address_book, args):
    name = args
    record = address_book.data[name]
    return f"Phone number(s) for {name}: {', '.join(str(phone) for phone in record.phones)}"


def handle_show_all(address_book, args):
    return str(address_book)


def main():
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ")
        action, args = command_parser(command)

        if action == "add":
            result = handle_add(address_book, args)
        elif action == "change":
            result = handle_change(address_book, args)
        elif action == "phone":
            result = handle_phone(address_book, args)
        elif action == "show all":
            result = handle_show_all(address_book, args)
        elif action == "exit":
            print("Good bye!")
            break
        else:
            result = "Invalid command. Please try again."

        print(result)


if __name__ == "__main__":
    main()