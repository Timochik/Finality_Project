def validate_phone_number(phone_number):
    # Видалити всі символи, які не є цифрами
    digits = ''.join(filter(str.isdigit, phone_number))
    
    # Перевірити, чи довжина номера телефону відповідає очікуваній
    return len(digits) == 10  # Наприклад, номер телефону складається з 10 цифр

def validate_email(email):
    # Перевірити, чи є символ '@' у рядку та чи є крапка після '@'
    return '@' in email and '.' in email[email.rindex('@'):]

# Приклад використання:

# Введення номера телефону та email
phone_number = input("Введіть номер телефону: ")
# Перевірка правильності введення
if validate_phone_number(phone_number):
    print("Номер телефону введено коректно.")
else:
    print("Некоректний формат номера телефону. В телефоні має бути як мінімум 10 цифр")
    input("Введіть номер телефону: ")

email = input("Введіть email: ")
# Перевірка правильності введення
if validate_email(email):
    print("Email введено коректно.")
else:
    print("Некоректний формат email. В імейлі має бути крапка та собачка @")
    input("Введіть email: ")


