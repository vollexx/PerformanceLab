import sys
import json


def load_json(file_path):
    '''Загружаем данные из JSON файла'''
    with open(file_path, 'r') as file:
        return json.load(file)


def create_value_dict(values):
    '''Создаем словарь для доступа к значениям по ID'''
    return {str(item['id']): item['value'] for item in values['values']}


def fill_report_structure(tests, values_dict):
    for test in tests:
        # Заполняем значения для текущего теста
        test_id = str(test['id']) # Преобразуем ID в строку
        test['value'] = values_dict.get(test_id, 'Unknown')

        # Обрабатываем вложенные под-тесты
        if 'values' in test:
            fill_report_structure(test['values'], values_dict)


def save_json(file_path, data):
    '''Сохраняем данные в JSON файл'''
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def main(values_file, tests_file, report_file):
    values = load_json(values_file)
    tests = load_json(tests_file)

    # Создаем словарь значений
    values_dict = create_value_dict(values)

    # Заполняем структуру тестов
    fill_report_structure(tests['tests'], values_dict)

    # Сохраняем отчет в report.json
    save_json(report_file, tests)


if __name__ == "__main__":
    # Проверка количества аргументов
    if len(sys.argv) != 4:
        print("Используйте: python script_name.py <values_file.json> <tests_file.json> <report_file.json>")
        sys.exit(1)

    # Пути к файлам
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    #Запуск основной программы
    main(values_file, tests_file, report_file)