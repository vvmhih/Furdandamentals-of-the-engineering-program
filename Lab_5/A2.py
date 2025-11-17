import re


def split_sentences(text):
    sentences = re.split(r'(?<=[.?!])\s+', text)

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return sentences


def main():
    text = input("Введите текст: ").strip()
    sentences = split_sentences(text)
    print("\nПредложения:")
    for sentence in sentences:
        print(sentence)
    print(f"\nПредложений в тексте: {len(sentences)}")

def split_sentences_manual(text):
    sentences = []
    current_sentence = ""

    for char in text:
        current_sentence += char
        if char in '.!?':
            sentences.append(current_sentence.strip())
            current_sentence = ""

    if current_sentence.strip():
        sentences.append(current_sentence.strip())

    return sentences

if __name__ == "__main__":

    test_text = "He jests at scars. That never felt a wound! Hello, friend! Are you OK?"

    print("Тестовый пример:")
    print(f"Ввод: {test_text}")

    sentences = split_sentences(test_text)

    print("\nВывод:")
    for sentence in sentences:
        print(sentence)
    print(f"Предложений в тексте: {len(sentences)}")

    print("\n" + "=" * 50)
    print("Дополнительные тесты:")

    test_cases = [
        "Первое предложение. Второе предложение! Третье предложение? Четвертое.",
        "Одно предложение.",
        "Много   пробелов   между   словами.   И   между   предложениями!   Проверка?",
        "Без знаков препинания",
        "Вопросительное? Восклицательное! Обычное.",
        "  Начинается с пробелов. Заканчивается пробелами  .  Еще одно!  ",
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        print(f"Ввод: '{test}'")
        sentences = split_sentences(test)
        print("Результат:")
        for j, sentence in enumerate(sentences, 1):
            print(f"  {j}. '{sentence}'")
        print(f"  Всего предложений: {len(sentences)}")

def explain_regex():

    print("\n" + "=" * 50)
    print("Объяснение регулярного выражения:")
    print("re.split(r'(?<=[.?!])\\s+', text)")
    print()
    print("(?<=[.?!]) - позитивный просмотр назад (positive lookbehind)")
    print("    Находит позицию, которой предшествует один из символов: . ! ?")
    print("\\s+ - один или более пробельных символов (пробелы, табуляции и т.д.)")
    print()
    print("Таким образом, регулярное выражение ищет места, где:")
    print("1. Есть один или более пробельных символов")
    print("2. Которые идут сразу после точки, восклицательного или вопросительного знака")
    print("3. Разделение происходит ПОСЛЕ пробелов, сохраняя знаки препинания в предложениях")

explain_regex()