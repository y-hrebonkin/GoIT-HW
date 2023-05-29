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
def create_contact_command(name, phone, contacts):
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' command to update the phone number."
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' created."

@input_error
def change_contact_command(name, phone, contacts):
    if name not in contacts:
        return f"Contact '{name}' does not exist. Use 'add' command to create a new contact."
    contacts[name] = phone
    return f"Phone number for contact '{name}' changed to '{phone}'."

@input_error
def get_phone_command(name, contacts):
    phone = contacts.get(name)
    if phone is None:
        return f"Contact '{name}' does not exist."
    return f"The phone number for contact '{name}' is '{phone}'."

def show_all_contacts_command(contacts):
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
        
        if command in ["hello", "hi", "привіт"]:
            response = hello_command()
        elif command.startswith("add"):
            _, name, phone = command.split()
            response = create_contact_command(name, phone, contacts)
        elif command.startswith("change"):
            _, name, phone = command.split()
            response = change_contact_command(name, phone, contacts)
        elif command.startswith("phone"):
            _, name = command.split()
            response = get_phone_command(name, contacts)
        elif command == "show all":
            response = show_all_contacts_command(contacts)
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            response = "Invalid command! Please try again."
        
        print(response)

# Запуск бота
main()