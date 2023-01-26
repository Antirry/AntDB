import json
from typing import Any, Union
import os
from AntFunction.AntFilters import int_key, check_dict_indexes_opers, check_string_filter


class AntDb:
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._db = {}
        self._load_db()

    def _load_db(self):
        if os.path.isfile(self._filename):
            self._db = json.load(open(self._filename))

    def _save(self) -> None:
        json.dump(self._db, open(self._filename, 'w'))

    def create_table(self, table_name: Union[str, int, float]) -> None:
        self._db[table_name] = {}
        self._save()

    def delete_table(self, table_name: Union[str, int, float]) -> bool:
        if table_name in self._db.keys():
            del self._db[table_name]
            self._save()
            return True
        return False

    def insert(self, table_name: Union[str, int, float], key: Union[str, int, float], value: Any) -> None:
        if not table_name in self._db.keys():
            self._db[table_name] = {}
        self._db[table_name][key] = value
        self._save()

    def get(self, table_name: Union[str, int, float], key: Union[str, int, float]) -> Any:
        if table_name in self._db.keys():
            return self._db[table_name].get(key)
        return None

    def delete(self, table_name: Union[str, int, float], key: Union[str, int, float]) -> Any:
        if table_name in self._db.keys():
            table = self._db[table_name]
            if key in table.keys():
                del table[key]
                self._save()
                return True
        return False

    def insert_many(self, table_name: Union[str, int, float],
                    keys_values_list: list[Union[str, int, float], Any]) -> None:
        if not table_name in self._db.keys():
            self._db[table_name] = {}
        init = iter(keys_values_list)
        keys_values_dict = dict(zip(init, init))
        self._db[table_name].update(keys_values_dict)
        self._save()

    def get_many(self, table_name: Union[str, int, float], keys_list: list[Union[str, int, float]]):
        if table_name in self._db.keys():
            return [self._db[table_name].get(k) for k in keys_list]
        return None

    def delete_many(self, table_name: Union[str, int, float], keys_list: list[Union[str, int, float]]) -> Any:
        if table_name in self._db.keys():
            table = self._db[table_name]
            keys_list = tuple(keys_list)
            if keys_list[0] in table.keys():
                all(map(table.pop, keys_list))
                self._save()
                return True
        return False

    def filter_key(self, table_name: Union[str, int, float], str_sort_key_with_comparison: str) -> Any:
        if table_name in self._db.keys():
            try:
                return int_key(self._db[table_name], str_sort_key_with_comparison)

            except Exception as ex:
                print("Ошибка фильтра -> ", ex)
                return None

    def filter_value(self, table_name: Union[str, int, float], str_sort_values_with_comparison: str) -> Any:
        if table_name in self._db.keys():
            try:
                return check_string_filter(str_sort_values_with_comparison, self._db[table_name])

            except Exception as ex:
                print("Ошибка фильтра -> ", ex)
                print("Возможно не тот тип данных (Исп. (int, float, str))")
                return None

    def many_filters_value(self, table_name: Union[str, int, float], str_logical_sort_oper_with_comparison: str) -> Any:
        if table_name in self._db.keys():
            try:
                str_indexes_opers_dict, list_words_oper_values = check_dict_indexes_opers(
                    str_logical_sort_oper_with_comparison)

                indexes = [i[0] for i in str_indexes_opers_dict.items()]
                opers = [i[1] for i in str_indexes_opers_dict.items()]
                i_val_dict = 0

                for index in indexes:
                    str_code = list_words_oper_values[index - 2] + " " + list_words_oper_values[index - 1]

                    locals()["dict_values" + str(i_val_dict)] = check_string_filter(str_code, self._db[table_name])
                    i_val_dict += 1

                str_code = list_words_oper_values[max(indexes) + 1] + " " + list_words_oper_values[
                    max(indexes) + 2]
                locals()["dict_values" + str(i_val_dict)] = check_string_filter(str_code, self._db[table_name])

                sort_dict_list = list()
                sort_dict_list.append(eval(fr'locals()["dict_values" + str({0})].items()' + ' ' + opers[
                    0] + ' ' + fr'locals()["dict_values" + str({0 + 1})].items()'))

                """
                range(len(opers)-1 так как я использовал одну переменную, поэтому я ее убираю,
                поэтому i+1 потому что мы посчитаем после одной логической операции (для зацикливания)
                
                (i+1)+1 так как мы считаем после двух переменных-операций со словарями
                """

                for i in range(len(opers)-1):
                    sort_dict_list.append(eval(f'sort_dict_list[{i}]' + ' ' + opers[
                        i + 1] + ' ' + f'locals()["dict_values" + str({(i + 1) + 1})].items()'))

                return dict(sort_dict_list[-1])

            except Exception as ex:
                print("Ошибка фильтра -> ", ex)
                print("Возможно не тот тип данных (Исп. (int, float, str))")
                return None
