from datetime import date, timedelta

def get_upcoming_birthdays(users, days_until_birthday):
    if not users:
        return []

    upcoming_birthdays = []

    today = date.today()
    year = today.year

    for user in users:
        name = user['name']
        #replace(year=year)- заміна на поточний рік
        birthday_date = user['birthday'].replace(year=year)

        # Перевірка, чи день народження вже минув у цьому році
        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_until_birthday_date = (birthday_date - today).days

        # Перевірка, чи день народження випадає через задану кількість днів
        if 0 <= days_until_birthday_date <= days_until_birthday:
            upcoming_birthdays.append({'name': name, 'birthday': birthday_date})

    return upcoming_birthdays

# Приклад використання функції зі списком користувачів і 7 днями до дня народження
users_list = [
    {'name': 'Valerii', 'birthday': date(year=2000, month=12, day=20)},
    {'name': 'Alice', 'birthday': date(year=2007, month=11, day=5)},
    
]

days_until_birthday = 7
upcoming_birthdays = get_upcoming_birthdays(users_list, days_until_birthday)

# Вивід результату
print(f"Контакти з днем народження через {days_until_birthday} днів:")
for contact in upcoming_birthdays:
    print(f"{contact['name']}: {contact['birthday']}")