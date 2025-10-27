def check_card_number(card_number):
    card_number = card_number.replace(' ', '')

    if not card_number.isdigit():
        return "Ошибка: номер должен содержать только цифры"

    length = len(card_number)

    if length == 15 and card_number.startswith(('34', '37')):
        card_type = "American Express"

    elif length == 16 and card_number.startswith(('51', '52', '53', '54', '55')):
        card_type = "MasterCard"

    elif card_number.startswith('4') and length in [13, 16]:
        card_type = "Visa"

    else:
        return "Неизвестный тип карты или неверная длина"

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    if total % 10 == 0:
        return f" Валидная карта {card_type}"
    else:
        return f" Невалидная карта {card_type}"

print("Проверка банковской карты")
print("=" * 30)

while True:
    card = input("\nВведите номер карты/выход: ").strip()

    if card.lower() in ['выход', 'exit', 'quit']:
        print("Программа завершена.")
        break

    result = check_card_number(card)
    print(f"Результат: {result}")