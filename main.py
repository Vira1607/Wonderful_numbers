print('Замечательные числа')

# Программа находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

for number in range(10, 100):
    candidate = number // 10 * number % 10 * 3
    if number == candidate:
        print(number)
