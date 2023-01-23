import json
from typing import Any, Union
import os


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

    def filter_key_db(self, table_name: Union[str, int, float], str_sort_key_with_comparison: str) -> Any:
        if table_name in self._db.keys():
            try:
                return dict(
                    filter(lambda elem: eval("elem[0] " + str_sort_key_with_comparison), self._db[table_name].items()))

            except Exception as ex:
                print("Ошибка фильтра -> ", ex)
                return None

    def filter_value_db(self, table_name: Union[str, int, float], str_sort_values_with_comparison: Any) -> Any:
        if table_name in self._db.keys():
            try:
                """ Для одного элемента
                return dict(filter(lambda elem: eval(str_sort_values + " elem[1]"), self._db[table_name].items()))"""

                """Для списка элементов"""
                if "in" in str_sort_values_with_comparison:
                    return dict(filter(lambda elem: any(eval(str_sort_values_with_comparison + " i") for i in elem[1]),
                                       self._db[table_name].items()))
                else:
                    return dict(filter(
                        lambda elem: any(
                            eval("i " + str_sort_values_with_comparison) for i in elem[1] if type(i) == int),
                        self._db[table_name].items()))

            except Exception as ex:
                print("Ошибка фильтра -> ", ex)
                return None
