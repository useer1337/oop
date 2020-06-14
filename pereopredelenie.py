class Person:
    def speak(self):
        return "Hello"


class Man(Person):
    def speak(self, word):
        return word


m = Person()

print(m.speak())

'''Доступ к методам базового класса!'''


class A:
    def say(self):
        return "A"


class B(A):
    def say_a(self):
        return super().say()

b = B()
print(b.say_a())
