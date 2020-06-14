class A:
    def __init__(self):
        self.x = 10

    def __str__(self):
        return f'Object x:{self.x}'

    def __add__(self, other):
        return self.x + other.x


a = A()
b = A()
print(a + b)
