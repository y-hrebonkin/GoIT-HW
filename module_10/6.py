class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"


cat = Cat("Simon", 10, "british")
print(cat.nickname)  # Виведе: Simon
print(cat.breed)  # Виведе: british
print(cat.weight)  # Виведе: 10

dog = Dog("Barbos", 23, "labrador")
print(dog.nickname)  # Виведе: Barbos
print(dog.breed)  # Виведе: labrador
print(dog.weight)  # Виведе: 23
