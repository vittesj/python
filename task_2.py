'''Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.'''

from random import randint, choice

min_ord = ord('a')
max_ord = ord('z')
min_len = 4
max_len = 7


def get_random_name():
    vowel_letters = set('aoueiy')
    name_len = randint(min_len, max_len)
    name = [chr(randint(min_ord, max_ord)) for _ in range(name_len)]
    if len(vowel_letters.intersection(set(name))) == 0:
        name[randint(0, len(name) - 1)] = choice(list(vowel_letters))
        name = ''.join(name)
        result = name.capitalize()
        return result


file_name = './data_task_2.txt'
m = 10
with open(file_name, 'w', encoding='utf-8') as f:
    for _ in range(m):
        f.write(f'{get_random_name()}\n')
