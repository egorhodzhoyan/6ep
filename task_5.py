number = 0
hidden_number = 7
attempt = 0
while number != hidden_number:
    number = int(input('Введите число: '))
    attempt += 1
    if number < hidden_number:
        print('Число меньше, чем нужно. Попробуйте еще раз!')
    elif number > hidden_number:
        print('Число больше, чем нужно. Попробуйте еще раз!')
    else:
        print('Вы угадали! Число попыток:', attempt)