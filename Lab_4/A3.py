def analyze_packet_loss():

    while True:
        packets = input("Ввод: ").strip()

        if len(packets) < 5:
            print("Ошибка: Длина последовательности должна быть не менее 5 символов!")
            print(f"Сейчас введено: {len(packets)} символов")
            continue

        if not all(char in '01' for char in packets):
            print("Неверный ввод. Используйте только символы '0' и '1'!")
            continue

        break

    total_packets = len(packets)
    lost_packets = packets.count('0')

    successful_packets = packets.count('1')

    max_lost_streak = 0
    current_streak = 0

    for packet in packets:
        if packet == '0':
            current_streak += 1
            if current_streak > max_lost_streak:
                max_lost_streak = current_streak
        else:
            current_streak = 0

    loss_percentage = (lost_packets / total_packets) * 100

    if loss_percentage <= 1:
        quality = "Отличное качество"
    elif loss_percentage <= 5:
        quality = "Хорошее качество"
    elif loss_percentage <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percentage <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
    print("=" * 60)
    print(f"Входная последовательность: {packets}")
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Успешно доставлено пакетов: {successful_packets}")
    print(f"Потеряно пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерь: {max_lost_streak}")
    print(f"Процент потерь: {loss_percentage:.2f}%")
    print(f"Оценка качества связи: {quality}")

if __name__ == "__main__":
    analyze_packet_loss()