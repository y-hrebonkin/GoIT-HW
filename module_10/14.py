class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        Contacts.current_id += 1

# У цьому коді клас Contacts містить змінну класу current_id, 
# яка слугує унікальним ідентифікатором для кожного контакту. 
# При створенні нового контакту у методі add_contacts створюється 
# словник із заданими ключами та значеннями, включаючи унікальний ідентифікатор.
# Цей словник додається до списку контактів self.contacts, а змінна current_id 
# збільшується на одиницю.
# Метод list_contacts просто повертає список контактів self.contacts.
# Ви можете створити екземпляр класу Contacts і викликати методи для 
# додавання контактів та отримання списку контактів. Наприклад:


# contacts = Contacts()

# contacts.add_contacts("John Doe", "(123) 456-7890", "john@example.com", True)
# contacts.add_contacts("Jane Smith", "(987) 654-3210", "jane@example.com", False)

# contact_list = contacts.list_contacts()
# for contact in contact_list:
#     print(contact)
    
# Вивід:

# {'id': 1, 'name': 'John Doe', 'phone': '(123) 456-7890', 'email': 'john@example.com', 'favorite': True}
# {'id': 2, 'name': 'Jane Smith', 'phone': '(987) 654-3210', 'email': 'jane@example.com', 'favorite': False}
# Таким чином, клас Contacts дозволяє додавати нові контакти і отримувати список наявних контактів.