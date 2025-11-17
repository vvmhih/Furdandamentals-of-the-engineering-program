def create_abbreviation(text):

    words = text.split()

    abbreviation = ''.join([word[0].upper() for word in words if len(word) >= 3])

    return abbreviation


def main():
    text = input("Введите текст: ").strip()

    abbreviation = create_abbreviation(text)

    print(f"Вывод: {abbreviation}")

def create_abbreviation_detailed(text):

    words = text.split()
    abbreviation = ""

    for word in words:

        if len(word) >= 3:

            first_letter = word[0].upper()
            abbreviation += first_letter

    return abbreviation

if __name__ == "__main__":
    test_cases = [
        "New York City",
        "Yanka Kupala State University of Grodno",
        "United Nations Educational Scientific and Cultural Organization",
        "World Health Organization",
        "Central Intelligence Agency",
        "a an the of in on at",
        "hello world",
        "I am a student",
        "  multiple   spaces   between   words  ",
        "",
    ]

    print("Тестирование программы:")
    print("=" * 50)

    for i, test in enumerate(test_cases, 1):
        result = create_abbreviation(test)
        print(f"Тест {i}:")
        print(f"  Ввод: '{test}'")
        print(f"  Вывод: '{result}'")
        print()



def create_abbreviation_advanced(text):

    if not text or text.isspace():
        return ""

    words = text.split()

    abbreviation = ''.join(word[0].upper() for word in words if len(word.strip()) >= 3)

    return abbreviation

def test_assignment_examples():

    print("Проверка примеров из задания:")
    print("=" * 30)

    example1 = "New York City"
    result1 = create_abbreviation(example1)
    print(f"Ввод: {example1}")
    print(f"Ожидаемый вывод: NYC")
    print(f"Фактический вывод: {result1}")
    print(f"Тест пройден: {result1 == 'NYC'}")
    print()

    example2 = "Yanka Kupala State University of Grodno"
    result2 = create_abbreviation(example2)
    print(f"Ввод: {example2}")
    print(f"Ожидаемый вывод: YKSUG")
    print(f"Фактический вывод: {result2}")
    print(f"Тест пройден: {result2 == 'YKSUG'}")
    print()

def explain_program():

    print("\nОбъяснение работы программы:")
    print("=" * 40)
    print("1. text.split() - разделяет строку на слова по пробелам")
    print("2. [word for word in words if len(word) >= 3] - фильтрует слова длиной 3+ символов")
    print("3. word[0].upper() - берет первую букву и преобразует в верхний регистр")
    print("4. ''.join(...) - объединяет все первые буквы в одну строку")
    print("\nПример:")
    text = "New York City"
    print(f"Исходный текст: '{text}'")
    words = text.split()
    print(f"Слова: {words}")
    filtered_words = [word for word in words if len(word) >= 3]
    print(f"Слова длиной >= 3: {filtered_words}")
    first_letters = [word[0].upper() for word in filtered_words]
    print(f"Первые буквы: {first_letters}")
    result = ''.join(first_letters)
    print(f"Результат: '{result}'")

test_assignment_examples()
explain_program()
print("\n" + "=" * 50)
print("Основная программа:")
main()