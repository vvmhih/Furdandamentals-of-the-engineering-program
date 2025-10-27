import string

def check_password_strength(password):
    #Проверяет надежность пароля и возвращает список ошибок
    errors = []

    # Проверка длины
    if len(password) != 8:
        errors.append("Длина пароля не равна 8")

    # Инициализация флагов
    flags = {
        'upper': False,
        'lower': False,
        'digit': False,
        'special': False,
        'invalid': False
    }

    # Проверка каждого символа
    for char in password:
        if char.isupper():
            flags['upper'] = True
        elif char.islower():
            flags['lower'] = True
        elif char.isdigit():
            flags['digit'] = True
        elif char in '*-#':
            flags['special'] = True
        else:
            flags['invalid'] = True

    # Добавление соответствующих ошибок
    if not flags['upper']:
        errors.append("В пароле отсутствуют заглавные буквы")
    if not flags['lower']:
        errors.append("В пароле отсутствуют строчные буквы")
    if not flags['digit']:
        errors.append("В пароле отсутствуют цифры")
    if not flags['special']:
        errors.append("В пароле отсутствуют специальные символы")
    if flags['invalid']:
        errors.append("В пароле используются непредусмотренные символы")

    return errors

password = input("Введите пароль: ")
errors = check_password_strength(password)

if not errors:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)
