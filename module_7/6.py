def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1] # перевернути рядок, якщо слово зашифроване у зворотньому порядку
    riddle = riddle.lower() # перевести все в рядку у нижній регістр для порівняння з літерами
    start_index = riddle.find(start_letter.lower()) # знайти індекс першої літери в рядку
    if start_index == -1: # якщо літеру не знайдено, повернути пустий рядок
        return ""
    for i in range(start_index, len(riddle) - word_length + 1):
        substring = riddle[i:i + word_length]
        if all(c.isalpha() for c in substring): # перевірити, що підрядок складається лише з літер
            return substring # повернути знайдене слово
    return "" # якщо жодне слово не знайдено, повернути пустий рядок
