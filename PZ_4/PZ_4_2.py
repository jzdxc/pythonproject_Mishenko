#Даны целые положительные числа A и B (A < B).
# Вывести все целые числа от A до B включительно;
# при этом каждое число должно выводиться столько раз, каково его значение
# (например, число 3 выводится 3 раза).
while True:
    try:
        a = int(input("Введите целое положительное число А: "))
        if a > 0:
            break
        print("Число А должно быть больше 0")
    except ValueError:
        print("Введите целое число.")
while True:
    try:
        b = int(input("Введите целое число B (B >A): "))
        if b > a:
            break
        print(f"Число в должно быть больше {a}!")
    except ValueError:
        print("Введите целое число.")
current_num = a
while current_num <= b:
    count = 0
    while count < current_num:
        print(current_num, end="")
        count += 1
    print()
    current_num += 1