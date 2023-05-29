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

def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone, contacts):
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' added."

@input_error
def change_contact(name, phone, contacts):
    contacts[name] = phone
    return f"Phone number for contact '{name}' changed to '{phone}'."

@input_error
def get_phone(name, contacts):
    phone = contacts[name]
    return f"The phone number for contact '{name}' is '{phone}'."

def show_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found."
    else:
        output = "Contacts:\n"
        for name, phone in contacts.items():
            output += f"{name}: {phone}\n"
        return output.strip()

def main():
    contacts = {}
    
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            response = hello()
        elif command.startswith("add"):
            _, name, phone = command.split()
            response = add_contact(name, phone, contacts)
        elif command.startswith("change"):
            _, name, phone = command.split()
            response = change_contact(name, phone, contacts)
        elif command.startswith("phone"):
            _, name = command.split()
            response = get_phone(name, contacts)
        elif command == "show all":
            response = show_all_contacts(contacts)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            response = "Invalid command! Please try again."
        
        print(response)

# Запуск бота
main()