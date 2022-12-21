import json


def get_menu_from_file(file_path=None) -> dict:
    """
    Функция которая считывает данные по меню
    в нашем случае файл локальный, но есть зазор под масштабирование
    (например брать файлы по api)
    """
    file = open(file_path, 'r', encoding='utf8')
    menu_data = json.loads(file.read())
    return menu_data
