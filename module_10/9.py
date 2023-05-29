from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


lookup_dict = LookUpKeyDict()
lookup_dict['a'] = 1
lookup_dict['b'] = 2
lookup_dict['c'] = 1

print(lookup_dict.lookup_key(1))  # ['a', 'c']
print(lookup_dict.lookup_key(2))  # ['b']
print(lookup_dict.lookup_key(3))  # []

# У цьому прикладі ми створили клас LookUpKeyDict, який успадковує клас UserDict. 
# В класі LookUpKeyDict ми додали метод lookup_key(), який приймає значення і повертає список ключів, 
# які мають це значення в словнику.
# При створенні екземпляру lookup_dict ми можемо додавати елементи до словника, 
# як до звичайного словника. Потім ми можемо викликати метод lookup_key() для пошуку ключів за значенням. 
# Результатом буде список ключів, які відповідають заданому значенню, або порожній список, якщо значення не знайдено в словнику.