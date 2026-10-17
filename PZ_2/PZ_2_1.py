# Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести результат
number = input("Дано трехзначное число: ")
while type(number) != int:
    try:
        if not number.isnumeric() or len(number) != 3:
            number = "error"
        number = int(number)
    except ValueError:
            print("Ошибка! Число должно быть трехзначным, без букв и символов.")
            number = input("Дано трехзначное число: ")
num_str = str(number)
result = num_str[1:] + num_str[0]
print(result)

3