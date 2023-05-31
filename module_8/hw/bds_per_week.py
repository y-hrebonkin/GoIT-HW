from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_per_day = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year)

        if start_of_week <= birthday <= end_of_week:
            if birthday.weekday() < 5:
                birthday_weekday = weekdays[birthday.weekday()]
                birthdays_per_day[birthday_weekday].append(name)
            elif birthday.weekday() == 5 or birthday.weekday() == 6:
                birthdays_per_day['Monday'].append(name)

    if today.weekday() == 0:
        yesterday = today - timedelta(days=1)
        before_yesterday = today - timedelta(days=2)
        for user in users:
            name = user['name']
            birthday = user['birthday'].replace(year=today.year)
            if birthday.date() == yesterday.date() or birthday.date() == before_yesterday.date():
                birthdays_per_day['Monday'].append(name)

    result = ""
    for weekday, birthdays in birthdays_per_day.items():
        if birthdays:
            birthday_names = ', '.join(birthdays)
            result += f"{weekday}: {birthday_names}\n"

    if result == "":
        result = "Немає користувачів для привітання на цьому тижні"

    return result

if __name__ == '__main__':
    # Тестовий список users
    users = [
        {'name': 'Anna', 'birthday': datetime(1985, 5, 29)},
        {'name': 'Sveta', 'birthday': datetime(1961, 5, 29)},
        {'name': 'Yura', 'birthday': datetime(1993, 5, 31)},
        {'name': 'Jenya', 'birthday': datetime(1989, 6, 2)},
        {'name': 'Artem', 'birthday': datetime(1990, 6, 5)},
        {'name': 'Oleksandr', 'birthday': datetime(1992, 6, 20)},
        {'name': 'Dmytro', 'birthday': datetime(1987, 5, 20)},
        {'name': 'Yuliia', 'birthday': datetime(2000, 5, 30)},
        {'name': 'Iryna', 'birthday': datetime(1992, 6, 5)},
        {'name': 'Olesya', 'birthday': datetime(1993, 6, 9)},
        {'name': 'Olia', 'birthday': datetime(1991, 6, 10)},
        {'name': 'Oleh', 'birthday': datetime(1985, 6, 6)},
        {'name': 'Vadym', 'birthday': datetime(1987, 6, 7)},
        {'name': 'Vitalii', 'birthday': datetime(1989, 6, 4)},
        {'name': 'Maryna', 'birthday': datetime(1990, 5, 28)},
        {'name': 'Svitlana', 'birthday': datetime(1978, 5, 27)},
        {'name': 'Alina', 'birthday': datetime(1995, 6, 2)},
        {'name': 'Olena', 'birthday': datetime(1984, 6, 3)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
