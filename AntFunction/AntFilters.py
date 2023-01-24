from typing import Any

""" Для одного элемента
return dict(filter(lambda elem: eval(str_sort_values + " elem[1]"), self._db[table_name].items()))"""

"""Для списка элементов"""


def int_key(table_dict: dict, str_sort_key_with_comparison: str) -> Any:
    return dict(
        filter(lambda i: eval(str_sort_key_with_comparison + " i[0]"),
               table_dict.items()))


def int_float_filter(table_dict: dict, str_sort_values_with_comparison: str) -> Any:
    return dict(filter(
        lambda elem: any(
            eval(str_sort_values_with_comparison + " i") for i in elem[1] if
            type(i) == int or type(i) == float), table_dict.items()))


def str_filter(table_dict: dict, str_sort_values_with_comparison: str) -> Any:
    return dict(filter(
        lambda elem: any(
            eval(str_sort_values_with_comparison + " i") for i in elem[1] if type(i) == str),
        table_dict.items()))