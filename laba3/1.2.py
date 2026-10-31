n =  int(input("Введите число n: "))
current_number = 1
step = 4

# Цикл работает до тех пор пока число НЕ станет больше n.
while current_number <= n:
    current_number += step
    step += 1

print("Первое число, большее n:", current_number)