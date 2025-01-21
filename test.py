number = int(input('Введите число: '))
decimal = 0
while number > 0:
  decimal += 1
  number = number // 10
print(decimal)