def decode(data):
    if not data:
        return []
    else:
        value = data[0]
        count = data[1]
        return [value] * count + decode(data[2:])

# Ця рекурсивна функція спершу перевіряє, чи список data порожній. Якщо так, то повертається порожній список.
# Якщо список не порожній, беруться перші два елементи списку: value (значення) та count (лічильник повторів). За допомогою оператора * формується список, в якому значення value повторюється count разів.
# Після цього викликається рекурсивна функція decode для решти списку data (починаючи з третього елемента), і результат додається до сформованого списку.