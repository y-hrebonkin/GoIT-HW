def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    
    with open(path, 'r') as file:
        file.seek(start_pos)
        result = file.read(count_chars)
    
    return result

# Параметр path є шляхом до файлу, в який буде записана додаткова інформація. 
# Параметр additional_info - це додаткова інформація, яку необхідно додати до файлу. 
# Параметр start_pos - це позиція в файлі, з якої починається зчитування рядка. 
# Параметр count_chars - це кількість символів, які потрібно зчитати з файлу. 
# Функція спочатку відкриває файл за допомогою контекстного менеджера with 
# зі значенням 'a' (append), що дозволяє додавати інформацію в кінець файлу. 
# Далі функція записує додаткову інформацію в файл. 
# Після цього функція знову відкриває файл за допомогою контекстного менеджера with
# зі значенням 'r' (read) і використовує методи seek та read для зчитування рядка 
# з позиції start_pos довжиною count_chars. Отриманий рядок повертається з функції.






