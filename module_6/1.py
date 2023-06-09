def total_salary(path):
    total = 0.0

    # відкриваємо файл для читання
    file = open(path, "r")

    # зчитуємо рядок з файлу
    line = file.readline()

    # працюємо з файлом, поки не досягнемо кінця файлу
    while line:
        # роздяляємо рядок на ім'я розробника та заробітну плату
        name, salary = line.split(",")

        # перетворюємо заробітну плату в число з плаваючою точкою та додаємо її до загальної суми
        total += float(salary)
        
        # зчитуємо наступний рядок з файлу
        line = file.readline()
    
    # закриваємо файл
    file.close()

    # повертаємо загальну суму заробітнох плати
    return total
