from pony.orm import *

db = Database()


class Person(db.Entity):
    id = PrimaryKey(int)
    name = Required(str)
    age = Required(int)


db.bind(provider='sqlite', filename='db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    p = Person(id=0, name="Саша", age=15)
    p = Person(id=1, name="Маша", age=16)
    p = Person(id=2, name="Саша", age=17)
    p = Person(id=3, name="Аша", age=15)

    # Person[0].age = 16 можно обновить значение атрибутов!
    # Person[0].delete() когда удаляем елементы!
    # person = Person[0]  # получение по id
    # person1 = Person.get(name="Маша")  # получение по атрибутам

    persons = select(p for p in Person).order_by(lambda p: (desc(p.age), p.name)).show()  # сортировка

    #print(person1.name)
    '''
    persons = select(p for p in Person)

    for p in persons:
        print(p.name + " " + str(p.age))
    '''
