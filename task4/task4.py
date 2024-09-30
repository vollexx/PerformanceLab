import sys


def read_numbers_from_file(file_path):
    '''Чтение целых чисел из файла'''
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def calculate_min_moves(nums):
    '''Расчет минимального значения ходов для приведения всех элементов к одному числу'''
    nums.sort() # Проводим сортировку для поиска медианы
    n = len(nums)

    # Поиск медианы
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = nums[n // 2 - 1]

    # Подсчет количества ходов
    moves = sum(abs(num - median) for num in nums)
    return moves


def main(file_path):
    # Считываем числа из файла
    nums = read_numbers_from_file(file_path)

    # Вычисляем минимальное количство ходов
    min_moves = calculate_min_moves(nums)

    # Вывод
    print(min_moves)


if __name__ == "__main__":
    # Проверка количества аргументов
    if len(sys.argv) != 2:
        print("Используйте: python script_name.py <file_path>")
        sys.exit(1)

    # Путь к файлу
    file_path = sys.argv[1]

    # Запускаем программу
    main(file_path)