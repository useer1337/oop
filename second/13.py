from pony.orm import Database, Optional, Required, db_session, Set

db = Database()


# Один к одному
class Men(db.Entity):
    # В ковычках поточу что еще не создан!
    wife = Optional('Women')


class Women(db.Entity):
    husband = Optional(Men)


# Один ко многим
class Women(db.Entity):
    children = Set('Child')


class Child(db.Entity):
    mother = Required(Women)


# Многие ко многим
class Product(db.Entity):
    tags = Set('Tag')


class Tag(db.Entity):
    products = Set(Product)


# Самоссылаемость
class Person(db.Entity):
    name = Required(str)
    spouse = Optional("Person", reverse="spouse")



db.bind(provider='sqlite', filename='db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    pass
