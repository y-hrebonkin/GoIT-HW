def is_integer(s):
    if not s or not s.strip(): # перевірка на порожній рядок або рядок з прогалин
        return False
    
    s = s.strip() # видаляємо початкові та кінцеві прогалини
    if len(s) == 1 and s.isdigit(): # якщо довжина дорівнює 1 та це цифра
        return True
    
    if s[0] in ["+", "-"]: # перевірка на наявність знаку "+/-"
        return s[1:].isdigit() # перевірка на наявність цифр у решті рядка
    
    return s.isdigit() # перевірка на наявність цифр у рядку