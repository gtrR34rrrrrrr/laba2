try:
    n = int(input("Введите число n: "))

    i = 1
    square = 1

    while square <= n:
        i += 1
        square = i * i

    
    print("Первое число, большее n:", square)

except ValueError:
    
    print("Ошибка! Пожалуйста, напишите цифры.")