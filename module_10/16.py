class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        return None

    def remove_contacts(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact["id"] != contact_id]

# У методі remove_contacts ми перебираємо список контактів self.contacts і залишаємо тільки ті контакти,
# чий ідентифікатор "id" не співпадає з переданим значенням contact_id. Таким чином, контакт зі співпадаючим
# ідентифікатором видаляється зі списку контактів.
# Ви можете створити екземпляр класу Contacts, додати кілька контактів, викликати метод remove_contacts
# для видалення контакту за його ідентифікатором і перевірити, що контакт був успішно видалений. Наприклад:

# contacts = Contacts()

# contacts.add_contacts("John Doe", "(123) 456-7890", "john@example.com", True)
# contacts.add_contacts("Jane Smith", "(987) 654-3210", "jane@example.com", False)

# print(contacts.list_contacts())
# # [{'id': 1, 'name': 'John Doe', 'phone': '(123) 456-7890', 'email': 'john@example.com', 'favorite': True},
# #  {'id': 2, 'name': 'Jane Smith', 'phone': '(987) 654-3210', 'email': 'jane@example.com', 'favorite': False}]

# contacts.remove_contacts(1)

# print(contacts.list_contacts())
# # [{'id': 2, 'name': 'Jane Smith', 'phone': '(987) 654-3210', 'email': 'jane@example.com', 'favorite': False}]
# У цьому прикладі ми створюємо екземпляр класу Contacts, додаємо два контакти до списку, викликаємо метод 
# remove_contacts для видалення контакту з ідентифікатором 1 і перевіряємо, що відповідний контакт був успішно
# видалений зі списку контактів.