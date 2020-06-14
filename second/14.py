from pony.orm import Database, Required, db_session

db = Database()


class Person(db.Entity):
    name = Required(str)


class Men(Person):
    pass


class Women(Person):
    pass


db.bind(provider='sqlite', filename='db', create_db=True)
db.generate_mapping(create_tables=True)

'''
with db_session:
    m = Men(name="Саша")
    w = Women(name="Маша")
    print(w.name)
'''


@db_session
def work_with_bd():
    m = Men(name="Саша")
    w = Women(name="Маша")
    print(w.name)


work_with_bd()
