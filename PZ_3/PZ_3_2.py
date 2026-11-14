# Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим)
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if (b <= a <= c) or (c <= a <= b):
    middle = a
elif (a <= b <= c) or (c <= b <= a):
    middle = b
else:
    middle = c

print("Исходные числа:", a, b, c)
print("Среднее число:", middle)
