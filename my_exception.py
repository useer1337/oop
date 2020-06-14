class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    raise MyException("Ошибка!!")
except MyException as m:
    print(m)
