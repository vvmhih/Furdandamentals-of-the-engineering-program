import random
import time


def multiplication_trainer():

    print("Тренажёр таблицы умножения")
    print("=" * 40)

    while True:
        try:
            n = int(input("Введите количество примеров: "))
            if n > 0:
                break
            else:
                print("Введите положительное число!")
        except ValueError:
            print("Введите целое число!")

    print(f"\nРешите {n} примеров:")
    print("=" * 40)

    correct_answers = 0
    total_time = 0
    results = []

    for i in range(n):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        correct_result = a * b

        print(f"\nПример {i + 1}/{n}: {a} × {b} = ?")

        start_time = time.time()

        while True:
            try:
                user_answer = input("Ваш ответ: ")
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Ошибка! Введите целое число.")
                print(f"Пример {i + 1}/{n}: {a} × {b} = ?")

        end_time = time.time()
        time_taken = end_time - start_time
        total_time += time_taken

        is_correct = user_answer == correct_result
        if is_correct:
            correct_answers += 1
            print("Верно!")
        else:
            print(f"Неверно. Правильно: {correct_result}")

        results.append({
            'example': f"{a} × {b}",
            'user_answer': user_answer,
            'correct_answer': correct_result,
            'time': time_taken,
            'is_correct': is_correct
        })

        print(f"Время: {time_taken:.1f} сек.")

    print("\n" + "=" * 50)
    print("СТАТИСТИКА")
    print("=" * 50)

    print(f"Общее время: {total_time:.2f} сек.")
    print(f"Среднее время на пример: {total_time / n:.2f} сек.")
    print(f"Правильных ответов: {correct_answers} из {n}")
    print(f"Процент правильных: {correct_answers / n * 100:.1f}%")

def main():
    multiplication_trainer()

if __name__ == "__main__":
    main()