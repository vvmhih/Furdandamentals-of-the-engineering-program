def draw_rectangle(n, m):

    print(f"\nПрямоугольник {n}x{m}:")
    for i in range(n):
        for j in range(m):
            print("*", end=" ")
        print()


def draw_right_triangle(n):

    print(f"\nПравый треугольник ({n} строк):")
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def draw_frame(n, m):

    print(f"\nРамка {n}x{m}:")
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def main():
    print("Генератор фигур с помощью вложенных циклов")
    print("=" * 40)

    try:
        n = int(input("Введите количество строк (n): "))
        m = int(input("Введите количество столбцов (m): "))

        if n <= 0 or m <= 0:
            print("Размеры должны быть положительными числами!")
            return

        draw_rectangle(n, m)
        draw_right_triangle(n)
        draw_frame(n, m)

    except ValueError:
        print("Ошибка! Введите целые числа.")

if __name__ == "__main__":
    main()