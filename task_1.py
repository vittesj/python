'''Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.'''

import json
from pathlib import Path

targ_file_name = './result.txt'
dest_file_name = './update.txt'


def parce_and_create(targ_file, dest_file):
    targ_file_name = Path(targ_file).resolve()
    dest_file_name = Path(dest_file).resolve()
    with open(targ_file, 'r', encoding='utf-8') as ft:
        result = {}
        for line in ft.readlines():
            k, v, *_ = line.split('|')
            k = k.capitalize()
            result[k] = float(v)
        with open(dest_file, 'w') as fd:
            json.dump(result, fd, indent=2, ensure_ascii=False)
        return


def main():
    parce_and_create(targ_file_name, dest_file_name)


if __name__ == '__main__':
    main()
