from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count


string = NumberString('Hello123World456')
print(string.number_count())  # 6

# У цьому прикладі ми створили клас NumberString, який успадковує клас UserString. 
# В класі NumberString ми визначили метод number_count(), який перераховує кількість
# цифр у рядку, представленому як self.data.
# При створенні екземпляру string ми передали рядок "Hello123World456" як аргумент.
# Потім ми викликаємо метод number_count() на цьому екземплярі, щоб отримати кількість цифр у рядку.
# У цьому прикладі результат буде 6, оскільки рядок містить шість цифр.