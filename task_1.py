number = int(input('Введите ваше число: '))
a = 0
while a < number:
    a += 1
    cube = a ** 3
    print('Ваш результат:')
    print(a, '** 3 =', cube)
