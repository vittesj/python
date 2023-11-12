'''Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.'''

import random


def generate_random_data_and_append(filename, num_lines):
    with open(filename, 'a') as file:
        for _ in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000.0, 1000.0)
            line = f'{int_num} | {float_num}\n'
            file.write(line)


generate_random_data_and_append('data.txt', 10)
