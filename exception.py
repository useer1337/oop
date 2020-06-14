a = 1
b = 0

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Мы попались!")
else:
    print("У нас все хорошо работает!")
finally:
    print("Я все ровно выполнюсь!")

print("hello")