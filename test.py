from main import AntDb


db = AntDb("db.json")


def test():
    db.create_table("T")
    db.insert("T", 1, "First Entry")
    db.insert("T", 2, "Second Entry")
    db.insert("T", 3, "Third Entry")
    print("Getting First Value: ", db.get("T", 1))
    db.insert("T", 4, "Fourth Entry")
    db.delete_key("T", 4)
    db.insert_many("T", [4, "Third Entry", 5, "Third Entry"])
    db.delete_many_key("T", [4, 5])
    print(db.get_many("T", [1, 2, 3]))
    print(db._db)
    print(db.filter_key("T", "2 <"))
    db.create_table("T1")
    db.insert_many("T1", [6, ["First Entry", 5, 'Ваф'], 7, ["Second Entry", 3.9], 8, ["Third Entry", 1]])
    print(db._db)
    print(db.filter_value("T1", "'Ваф' in"))
    print(db.filter_value("T1", "3 <"))

    db.insert("T1", 10, 'Fiftieth Entry')

    db.edit_value('T', 1, 'rsw')
    db.edit_values_many('T', [1, 'First VALUE', 2, 'Second VALUE', 3, 'Third VALUE'])

    print("\n Для нескольких фильтров \n")
    print(dict(db.filter_value("T1", "'Ent' in").items())
          or dict(db.filter_value("T1", "'Th' in")).items()
          or dict(db.filter_value("T1", "'f' in")).items())

    print('\n\n\n\n')

    print(db.many_filters_value("T1", "'Ent' in or 'Th' in or 'f' in"))

    print(db.many_filters_value("T", "'Ent' in or 'Th' in"))

    """
    СДЕЛАТЬ ФУНКЦИЮ С В main.py где будет редактирование ключей, значений словаря
    
    как AntFunction.AntFilters.edit_one_to_list_val()
    """


def Test1():
    print("\n\n Вывесьти таблицу \n\n")
    print(db._db)
    print(db._db['T'])
    print(db._db['T1'])


test()
Test1()

