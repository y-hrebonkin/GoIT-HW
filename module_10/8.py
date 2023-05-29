class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class Dog(Animal):
    def say(self):
        return "Woof"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class CatDog(Cat, Dog):
    pass


class DogCat(Dog, Cat):
    pass


cat_dog = CatDog("Kitty", 5)
dog_cat = DogCat("Buddy", 10)

print(cat_dog.say())  # Виведе: Meow
print(dog_cat.say())  # Виведе: Woof

print(cat_dog.info())  # Виведе: Kitty-5
print(dog_cat.info())  # Виведе: Buddy-10

# У цьому прикладі класи CatDog та DogCat успадковуються від класів Cat та Dog відповідно. 
# Класи Cat і Dog мають свої власні реалізації методу say(), які повертають "Meow" і "Woof" відповідно. 
# Також вони мають метод info(), який повертає рядок з інформацією про кота або собаку.
# При створенні екземплярів cat_dog і dog_cat відповідно, ви можете викликати метод say()
# для отримання звуку, який видаватимуть ці комбіновані тварини. Виклик методу info()
# дозволяє отримати рядок з інформацією про прізвисько та вагу кота або собаки.