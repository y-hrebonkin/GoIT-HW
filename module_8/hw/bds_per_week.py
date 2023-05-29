from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    start_of_week = current_date - timedelta(days=current_date.weekday())

    birthdays_per_week = {i: [] for i in range(7)}

    for user in users:
        birthday = user['birthday'].date()
        diff = (birthday - start_of_week).days

        if diff >= 5:  # Включаємо суботу та неділю
            diff = (diff + 7 - start_of_week.weekday()) % 7
            if diff == 0:
                diff = 7

        if 0 <= diff < 7:
            greeting_day = (start_of_week + timedelta(days=diff)).strftime('%A')
            birthdays_per_week[diff].append(user['name'])

    for diff, names in birthdays_per_week.items():
        if names:
            greeting_day = (start_of_week + timedelta(days=diff)).strftime('%A')
            print(f"{greeting_day}: {', '.join(names)}")

# Приклад використання
users = [
    {'name': 'Anna', 'birthday': datetime(1985, 5, 29)},
    {'name': 'Sveta', 'birthday': datetime(1961, 5, 29)},
    {'name': 'Yura', 'birthday': datetime(1993, 5, 31)},
    {'name': 'Jenya', 'birthday': datetime(1989, 6, 2)},
    {'name': 'John', 'birthday': datetime(1990, 6, 5)},
    {'name': 'Kate', 'birthday': datetime(1992, 6, 7)},
]

get_birthdays_per_week(users)
