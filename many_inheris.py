class A:
    def hi(self):
        return "A"


class B(A):
    def hi(self):
        return "B"


class C(A):
    def hi(self):
        return "C"


class D(B, C):
    pass;

d = D()

print(D.mro())


