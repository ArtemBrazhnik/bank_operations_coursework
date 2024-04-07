import json
from datetime import datetime


def loading_json(filename):
    """загрузить данные из файла"""
    with open (filename, 'r', encoding='utf-8') as load_file:
        return json.load(load_file)


def filter_list(load_file):
    """сортировка по фильтру"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective


def sort_by_date(json_adjective):
    """сортировка по дате"""
    return sorted(json_adjective, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)


def date_format(date):
    """форматирование вида даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


def hide_num(num):
    """скрытие номера карты и счёта"""
    req = num.split()
    if req[0] == "Счет":
        return f"Счет **{req[-1][-4:]}"
    else:
        card_name = " ".join(req[:-1])
        return f"{card_name} {req[-1][:4]} {req[-1][4:6]}** **** {req[-1][-4:]}"


def format_sum(cash):
    """форматирование вида суммы операции"""
    return f"{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}"


def get_main(num_operations=5):
    """вывод операций"""
    load_json = loading_json("operations.json")
    filter = filter_list(load_json)
    sort = sort_by_date(filter)
    for operation in sort:
        if num_operations == 0:
            break
        print(date_format(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(hide_num(operation["from"]) + " -> ", end="")
        print(hide_num(operation["to"]))
        print(format_sum(operation), "\n")
        num_operations -= 1
