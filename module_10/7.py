class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Barbos", 23, "labrador", owner)

print(dog.nickname)  # Виведе: Barbos
print(dog.breed)  # Виведе: labrador
print(dog.weight)  # Виведе: 23

owner_info = dog.who_is_owner()
print(owner_info)  # Виведе: {'name': 'Sherlock', 'age': 24, 'address': 'London, 221B Baker Street'}

# У класі Owner ми додали метод info(), який повертає словник з інформацією про власника собаки. 
# В класі Dog ми додали атрибут owner, який є екземпляром класу Owner. 
# Метод who_is_owner() викликає метод info() екземпляра owner і повертає результат.
# При створенні екземпляру dog з використанням конструктора Dog("Barbos", 23, "labrador", owner),
# ви можете отримати доступ до властивостей nickname, weight і breed для об'єкту dog, а також 
# викликати метод who_is_owner() для отримання інформації про власника.