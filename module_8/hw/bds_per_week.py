from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = defaultdict(list)
    
    for user in users:
        birthday = user['birthday'].date()
        if birthday >= today and birthday <= next_week:
            day_of_week = weekdays[birthday.weekday()]
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthdays[day_of_week].append(user['name'])
    
    for day in weekdays:
        if day in birthdays:
            print(f"{day}: {', '.join(birthdays[day])}")