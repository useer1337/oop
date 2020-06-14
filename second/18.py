from pony.orm import *

db = Database()


class Person(db.Entity):
    name = Required(str)
    age = Required(int)


class Parent(Person):
    children = Set('Children')


class Children(Person):
    parent = Required(Parent)


db.bind(provider='sqlite', filename='db', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(False)

with db_session:
    parent = Parent(name='Родитель1', age=54)
    parent1 = Parent(name='Родитель2', age=34)
    parent2 = Parent(name='Родитель3', age=35)
    child1 = Children(name='Ребенок1', parent=parent, age=5)
    child2 = Children(name='Ребенок2', parent=parent, age=10)
    child3 = Children(name='Ребенок3', parent=parent, age=15)

    # суммарный возраст всех людей
    s = sum(p.age for p in Person)
    print(s)

    # самый молодой человек
    print(min(p.age for p in Person))

    # самый старый человек
    print(max(p.age for p in Person))

    # средний возраст людей
    print(avg(p.age for p in Person))

    # кол-во людей
    print(count(p for p in Person))

    # group_concat
    # group_concat(p.name for p in Person, sep="-")

    # агрегатные методы!

    query = select(p.age for p in Parent)
    print(query.max())

    # условыный count показать с show()
    query = select((p, count(p.age < 50),
                    count(p.age > 30)) for p in Person).show()

    query1 = select(p for p in Parent if len(p.children) != 0).order_by(lambda p: max(p.age)).show()
