# Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим)
while True:
    try:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        c = int(input("Третье число: "))
        break
    except ValueError:
        print("Неправильно ввел. Введи целые числа заново.")
if (b <= a <+ c) or (c <= a <= b):
    middle = a
elif (a <= b <= c) or (b <= c <= a):
    middle = b
else:
    middle = c
print("Исходные числа:", a, b, c)
print ("Среднее число:", middle)