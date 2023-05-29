from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now().date()
    # Визначаємо початок тижня (понеділок)
    start_of_week = current_date - timedelta(days=current_date.weekday())
    
    # Створюємо словник для збереження користувачів за днями тижня
    birthdays_per_week = {i: [] for i in range(7)}
    
    # Проходимося по кожному користувачеві
    for user in users:
        # Отримуємо день народження користувача
        birthday = user['birthday'].date()
        
        # Обчислюємо різницю між днем народження та початком тижня
        diff = (birthday - start_of_week).days
        
        # Перевіряємо, чи день народження впадає на поточний або наступний тиждень
        if 0 <= diff < 7:
            # Визначаємо день тижня для вітання
            greeting_day = (start_of_week + timedelta(days=diff)).strftime('%A')
            # Додаємо користувача до списку іменинників у відповідний день
            birthdays_per_week[diff].append(user['name'])
    
    # Виводимо список іменинників по днях тижня
    for diff, names in birthdays_per_week.items():
        if names:
            greeting_day = (start_of_week + timedelta(days=diff)).strftime('%A')
            print(f"{greeting_day}: {', '.join(names)}")

# Приклад використання
users = [
    {'name': 'Anna', 'birthday': datetime(2023, 5, 29)},
    {'name': 'Sveta', 'birthday': datetime(2023, 5, 29)},
    {'name': 'Yura', 'birthday': datetime(2023, 5, 31)},
    {'name': 'Jenya', 'birthday': datetime(2023, 6, 2)},
]

get_birthdays_per_week(users)