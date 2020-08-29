num = int(input('Введите число: '))
k = 0
while num > 0:
    if k < (num % 10):
        k = num % 10
    num //= 10
print(f'Наибольшая цифра в числе равна {k}')
