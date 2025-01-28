number = int(input('Введите ваше число: '))
amount = 0
if number > 0:
    while number > 0:
        number //= 10
        amount += 1
    print('Количество цифр в числе:', amount)
elif number == 0:
    amount += 1
    print('Количество цифр в числе:', amount)
else:
    print('Недопустимое число!')