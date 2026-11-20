# Дано вещественное число X и целое число N (> 0).
# Найти приближенное значение функции exp в точке X.
x = input("Введи вещественное число X: ")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввел")
        x = input("Введи вещественное число X: ")

n = input("Введи целое число N (> 0): ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввел")
        n = input("Введи целое число N (> 0): ")
s = 1.0
p = 1.0
f = 1
i = 1
while i <= n:
    p *= x
    f *= i
    s += p / f
    i += 1
print("Результат:", s)