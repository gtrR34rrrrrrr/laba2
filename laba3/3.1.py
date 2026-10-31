try:
    #безопасный ввод размера массива
    correct_n = False
    N = 0
    while not correct_n:
        try:
            N = int(input("Введите количество элементов массива N: "))
            if N > 0:
                correct_n = True
            else:
                print("Количество элементов должно быть больше 0!")
        except ValueError:
            print("Ошибка! Введите целое число.")

    arr = []
    i = 0
    while i < N:
        try:
            element = float(input(f"Введите элемент {i}: "))
            arr.append(element)
            i += 1
        except ValueError:
            print("Ошибка! Введите число.")

    min_mod_element = min(arr, key=abs)
    
    print("\nИсходный массив:", arr)
    print("Минимальный по модулю элемент:", min_mod_element)

    reversed_arr = arr[::-1]
    print("Массив в обратном порядке:", reversed_arr)

except Exception:
    print("ERROR")