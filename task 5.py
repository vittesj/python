revenue = int(input('Введите вашу выручку: '))
cost = int(input('Введите ваши издержки: '))
if revenue > cost:
    print('Фирма оказалась в прибыли')
    profitability = (revenue - cost) / revenue * 100
    print(f'Рентабельность фирмы составляет {profitability}%')
    k = int(input('Введите колличество сотрудников фирмы: '))
    print('Прибыль каждого сотрудника фирмы составляет: ', (revenue - cost) / k)
elif revenue == cost:
    print('Фирма не получила прибыли, но и не понесла убытков')
else:
    print('Фирма понесла убыток')
