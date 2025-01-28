deposit = int(input('Введите сумму на вкладе в банке: '))
percent = int(input('Введите под какой процент вложены средства: '))
limit_deposit = int(input('Введите порог вклада: '))
years = 0
while deposit < limit_deposit:
    count = (deposit * percent // 100)
    years += 1
    if years > 1:
        deposit += count
    print(years, 'год.', deposit, '+', percent, '% =', deposit + count)
    if deposit + count >= limit_deposit:
        break
print('Количество лет для достижения порога:', years)