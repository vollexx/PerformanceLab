import sys


def circular_array_path(n, m):
    # Массив от 1 до n
    array = list(range(1, n + 1))

    # Путь, начинаем с 1-го элемента (индекс 0)
    path = []
    current_index = 0

    # Добавляем первый элемент в путь
    while array[current_index] not in path:
        path.append(array[current_index])

        # Рассчитываем следующий индекс с использованием кругового массива
        current_index = (current_index + m - 1) % n

    # Выводим результат
    return ''.join(map(str, path))


if __name__ == "__main__":
    # Чтение аргументов командной строки
    if len(sys.argv) != 3:
        print("Введите два аргумента: n и m.")
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])

            # Проверка на корректность введенных данных
            if n <= 0 or m <= 0:
                print("n и m должны быть положительными числами.")
            else:
                # Выводим путь
                print(circular_array_path(n, m))

        except ValueError:
            print("n и m должны быть целыми числами.")
