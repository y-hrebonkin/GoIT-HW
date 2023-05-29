class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Animal sound"

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat("Simon", 10)
print(cat.nickname)  # Виведе: Simon
print(cat.weight)  # Виведе: 10
print(cat.say())  # Виведе: Meow
