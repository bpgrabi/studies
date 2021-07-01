lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError:
    print("wrong index, check it")

try:
    print(5/0)
except ZeroDivisionError:
    print("dont division by zero, its illegal")

try:
    print(lis)
except NameError:
    print("wrong name, check it")
