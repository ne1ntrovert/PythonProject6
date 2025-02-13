from typing import Any, List

def filter_by_state(list_of_dicts: list[Any], state: str = "EXECUTED") -> list[Any]:
    """Проверяет значение в словарях на заданное и если оно совпадает то, выводит его"""
    correct_list = []
    for num_dict in range(len(list_of_dicts)):  # Исправлено здесь
        if list_of_dicts[num_dict]["state"] == state:
            correct_list.append(list_of_dicts[num_dict])
    return correct_list


def sort_by_date(list_of_dicts: List[dict[str, Any]], sorting_direct: bool = True) -> List[dict[str, Any]]:
    """Сортирует список словарей по датам."""
    return sorted(list_of_dicts, key=lambda x: x.get("date"), reverse=not sorting_direct)



print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, descending=True):
    """
    Сортирует список словарей по значению ключа 'date'
    """
    # Преобразуем строку даты в объект datetime для корректной сортировки
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)


def mask_account_card(card_info):
    """
    Принимает строку формата "Visa Platinum 7000792289606361", "Maestro 7000792289606361" и "Счет 73654108430135874305"
    """
    if "Счет" in card_info:
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)


def get_date(date_str):
    """
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    try:
        date_part = date_str.split('T')[0]
        year, month, day = date_part.split('-')
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Неверный формат даты")


def get_mask_card_number(card_info):
    """
    Принимает на вход строку с типом и номером карты и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    parts = card_info.split()
    card_number = parts[-1]
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return ' '.join(parts[:-1]) + ' ' + masked_number


def get_mask_account(account_info):
    """
    Принимает на вход строку с типом и номером счета и возвращает маску номера по правилу **XXXX
    """
    parts = account_info.split()
    account_number = parts[-1]
    if len(account_number) < 6:
        raise ValueError("Номер счета должен содержать не менее 6 цифр.")
    masked_number = f"**{account_number[-4:]}"
    return ' '.join(parts[:-1]) + ' ' + masked_number
