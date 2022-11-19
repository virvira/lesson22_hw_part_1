# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv_file = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(_csv_file):
    """Чтение данных из строки"""
    data = []
    for line in _csv_file.split("\n"):
        item = line.split(";")
        data.append(item)
    return data


def take_age(list_item):
    """Функция возвращает второй элемент подсписка в списке"""
    return int(list_item[1])


def _sort(data):
    """Сортировка по возрасту по возрастанию"""
    sorted_data = sorted(data, key=take_age, reverse=False)
    return sorted_data


def _filter(_new_data):
    """Фильтрация"""
    result_data = filter(lambda item: int(item[1]) >= 10, _new_data)
    return list(result_data)


def get_users_list():
    """Получение списка пользователей"""
    data = _read(csv_file)
    sorted_data = _sort(data)
    result_data = _filter(sorted_data)
    return result_data


if __name__ == '__main__':
    print(get_users_list())
