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
# set_sql_debug(True)

with db_session:
    parent = Parent(name='Родитель1', age=54)
    parent1 = Parent(name='Родитель2', age=34)
    parent2 = Parent(name='Родитель3', age=35)
    child1 = Children(name='Ребенок1', parent=parent, age=5)
    child2 = Children(name='Ребенок2', parent=parent, age=10)
    child3 = Children(name='Ребенок3', parent=parent, age=15)

    query1 = select(c for c in Children if c.parent == Parent.get(name='Родитель1'))
    # так как позвращает query можно к нему применять методы
    obj = query1.first()
    query2 = query1.filter(lambda ch: ch.age > 5)
    # использовать запрос в другом запросе!
    query3 = select(c.name for c in query1).show()

    # другие запросы!

    # самый большой возраст родителя
    var = max(p.age for p in Parent)
    print(var)

    # самый большой возраст среди людей не старше 50
    var1 = max(p.age for p in Parent if p.age < 50)
    print(var1)

    # родители у которых нет детей по убыванию в плане возраста
    select(p for p in Parent if len(p.children) == 0).order_by(lambda p: desc(p.age)).show()

    # raw_sql
    # все люди возраст которых меньше 50
    select(p for p in Person if raw_sql('abs("p"."age")<50')).show()

    # select_by_sql
    # все родители младше 50 лет!
    select(p for p in Parent).show()
    parents = Person.select_by_sql(
        "SELECT * FROM \"Person\" WHERE \"Person\".\"classtype\" IN ('Parent') AND abs(\"Person\".\"age\")<50")
    print(parents)

    # select(p for p in Person).show()
