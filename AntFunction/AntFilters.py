from typing import Any

""" Для одного элемента
return dict(filter(lambda elem: eval(str_sort_values + " elem[1]"), self._db[table_name].items()))"""

"""Для списка элементов"""


def int_key(table_dict: dict, str_sort_key_with_comparison: str) -> Any:
    return dict(
        filter(lambda i: eval(str_sort_key_with_comparison + " i[0]"),
               table_dict.items()))


def edit_one_to_list_val(table_dict: dict) -> Any:
    dict_val_list = {k: [''.join(word) for word in zip(*list(v))] for k, v in table_dict.items() if type(v) is not list}

    table_dict.update(dict_val_list)

    return table_dict


def int_float_filter_list_val(table_dict: dict, str_sort_values_with_comparison: str) -> Any:
    return dict(filter(
        lambda elem: any(
            eval(str_sort_values_with_comparison + " i") for i in elem[1] if
            type(i) == int or type(i) == float), table_dict.items()))


def str_filter_list_val(table_dict: dict, str_sort_values_with_comparison: str) -> Any:
    return dict(filter(
        lambda elem: any(
            eval(str_sort_values_with_comparison + " i") for i in elem[1] if type(i) == str),
        table_dict.items()))


def check_dict_indexes_opers(str_logical_sort_oper_with_comparison: str) -> list[dict, list]:
    list_words_oper_values = str_logical_sort_oper_with_comparison.split()

    logic_oper_list = ['and', 'or', 'not']
    str_indexes_opers_dict = {i: list_words_oper_values[i] for i in range(len(list_words_oper_values)) if
                              list_words_oper_values[i] in logic_oper_list}

    return [str_indexes_opers_dict, list_words_oper_values]


def list_check_string_filter(str_code: str, table_dict: dict) -> Any:
    string_numbers = any(e.isdigit() for e in str_code)

    if string_numbers is True:
        return int_float_filter_list_val(edit_one_to_list_val(table_dict), str_code)
    else:
        return str_filter_list_val(edit_one_to_list_val(table_dict), str_code)
