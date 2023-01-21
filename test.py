from main import AntDb


def test():
    db = AntDb("db.json")

    db.create_table("T")
    db.insert("T", 1, "First Entry")
    db.insert("T", 2, "Second Entry")
    db.insert("T", 3, "Third Entry")
    print("Getting First Value: ", db.get("T", 1))
    db.insert("T", 4, "Fourth Entry")
    db.delete("T", 4)
    db.insert_many("T", [4, "Third Entry", 5, "Third Entry"])
    db.delete_many("T", [4, 5])
    print(db.get_many("T", [1, 2, 3]))
    print(db._db)


test()

