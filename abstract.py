from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def hello(self):
        pass


class B(A):
    def hello(self):
        return 'hello'


b = B()
print(b.hello())
