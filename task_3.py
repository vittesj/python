'''Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.'''


def multiply_and_save():
    with open('data.txt', 'r') as data, open('data_task_2.txt', 'r') as names, open('result.txt', 'w') as output:
        lines1 = data.readlines()
        lines2 = names.readlines()
        max_lines = max(len(lines1), len(lines2))
        for i in range(max_lines):
            line1 = lines1[i % len(lines1)].strip()
            line2 = lines2[i % len(lines2)].strip()
            num1, num2 = line1.split(' |')
            num2 = float(num2)
            num1 = int(num1)
            result = num1 * num2
            if result < 0:
                line2 = line2.lower()
                result = abs(result)
            else:
                line2 = line2.upper()
                result = round(result)
            output.write(f'{line2} | {result}\n')


multiply_and_save()
