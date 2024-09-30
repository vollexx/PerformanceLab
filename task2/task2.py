import sys
import math


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        # Читаем координаты центра и радиус
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (center_x, center_y, radius)


def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def point_position(circle, points):
    center_x, center_y, radius = circle
    results = []

    for (x, y) in points:
        # Вычисляем расстояние от точки до центра окружности
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

        # Определяем положение точки относительно окружности
        if distance < radius:
            results.append(1)  # Точка внутри
        elif distance == radius:
            results.append(0)  # Точка на окружности
        else:
            results.append(2)  # Точка снаружи

    return results


if __name__ == "__main__":
    # Проверка количества аргументов командной строки
    if len(sys.argv) != 3:
        print("Используйте: python script_name.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Считываем данные
    circle = read_circle_data(circle_file)
    points = read_points(points_file)

    # Получаем положение точек относительно окружности
    positions = point_position(circle, points)

    # Выводим результаты
    for position in positions:
        print(position)
