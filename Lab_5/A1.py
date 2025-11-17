def shorten_text(text):

    result = text

    while True:

        left_bracket = result.find('(')
        right_bracket = result.find(')')

        if left_bracket != -1 and right_bracket != -1 and right_bracket > left_bracket:
            result = result.replace(result[left_bracket:right_bracket + 1], '')
        else:
            break

    return result

def shorten_text_rfind(text):
    result = text

    while True:
        left_bracket = result.find('(')

        if left_bracket == -1:
            break

        right_bracket = result.find(')', left_bracket)

        if right_bracket == -1:
            break

        result = result.replace(result[left_bracket:right_bracket + 1], '')

    return result



if __name__ == "__main__":
    original_text = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())."

    shortened_text = shorten_text(original_text)

    print("Исходный текст:", original_text)
    print("Укороченный текст:", shortened_text)

    test_cases = [
        "Простой (текст в скобках) пример",
        "Текст без скобок",
        "Много (вложенных (скобок)) тест",
        "Только (открывающая скобка",
        "Только закрывающая) скобка",
        "Пустые () скобки",
        "(Начинается со скобки) текст",
        "Текст (заканчивается скобкой)"
    ]

    print("\nДополнительные тесты:")
    for test in test_cases:
        result = shorten_text(test)
        print(f"'{test}' -> '{result}'")