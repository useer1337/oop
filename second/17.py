from pony.orm import *

db = Database()


class Parent(db.Entity):
    name = Required(str)
    children = Set("Child", cascade_delete=False)


class Child(db.Entity):
    name = Required(str)
    age = Required(int)
    parent = Optional(Parent)


db.bind(provider='sqlite', filename='db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    parent1 = Parent(name="Родитель1")
    child1 = Child(name="Ребенок1",  age=11)
    child2 = Child(name="Ребенок2",  age=12)

    parent1.children.add(child1)
    parent1.children.add(child2)

    select(p for p in Parent).show()
    select(c for c in Child).show()

    parent1.children.select(lambda c: c.age > 11).show()
