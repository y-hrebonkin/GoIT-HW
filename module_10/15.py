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

# У методі get_contact_by_id ми перебираємо список контактів self.contacts
# і порівнюємо значення ключа "id" зі значенням, переданим у параметрі contact_id.
# Якщо знайдено контакт зі співпадаючим ідентифікатором, повертається відповідний 
# словник контакту. Якщо контакт з таким ідентифікатором не знайдено, повертається None.
# Ви можете створити екземпляр класу Contacts, додати кілька контактів і викликати метод
# get_contact_by_id для отримання контакту за його ідентифікатором. 

# contacts = Contacts()

# contacts.add_contacts("John Doe", "(123) 456-7890", "john@example.com", True)
# contacts.add_contacts("Jane Smith", "(987) 654-3210", "jane@example.com", False)

# contact = contacts.get_contact_by_id(1)
# print(contact)  # {'id': 1, 'name': 'John Doe', 'phone': '(123) 456-7890', 'email': 'john@example.com', 'favorite': True}

# contact = contacts.get_contact_by_id(3)
# print(contact)  # None
# У цьому прикладі ми спочатку додаємо два контакти до класу Contacts, 
# а потім викликаємо метод get_contact_by_id з різними ідентифікаторами. 
# Один контакт знайдено і виведено, а для іншого отримано значення None,
# оскільки контакту з таким ідентифікатором не існує.