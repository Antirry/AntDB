from main import AntDb


def test():
    db = AntDb("db.json")
    #
    # db.create_table("T")
    # db.insert("T", 1, "First Entry")
    # db.insert("T", 2, "Second Entry")
    # db.insert("T", 3, "Third Entry")
    # print("Getting First Value: ", db.get("T", 1))
    # db.insert("T", 4, "Fourth Entry")
    # db.delete("T", 4)
    # db.insert_many("T", [4, "Third Entry", 5, "Third Entry"])
    # db.delete_many("T", [4, 5])
    # print(db.get_many("T", [1, 2, 3]))
    # print(db._db)
    # print(db.filter_key("T", "2 <"))
    # db.create_table("T1")
    # db.insert_many("T1", [6, ["First Entry", 5, 'Ваф'], 7, ["Second Entry", 3.9], 8, ["Third Entry", 1]])
    # print(db._db)
    # print(db.filter_value("T1", "'Ваф' in"))
    # print(db.filter_value("T1", "3 <"))
    #
    print("Для нескольких фильтров")
    print(dict(db.filter_value("T1", "'Ваф' in").items())
          and dict(db.filter_value("T1", "'Sec' in").items())
          and dict(db.filter_value("T1", "5 <"))
          or dict(db.filter_value("T1", "'Ваф' in").items()))

    print('\n\n\n\n')

    print(db.many_filters_value("T1", "'Ваф' in and 'Sec' in and 5 < or 'Ваф' in"))

    """СДЕЛАТЬ ДЛЯ ПЕРЕМЕННЫХ, А НЕ СПИСКОВ"""
    # print(db.many_filters_value("T", "'Sec' in or 'Fir' in or 'Th' in"))


test()

