'''Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.'''

import os
from pathlib import Path

VIDEO_FOLDER_NAME = 'video'
TEXT_FOLDER_NAME = 'txt'


def sort_files(path):
    p = Path(path)
    for el in p.iterdir():
        suffix = Path(el).suffix[1:]
        if el.is_file() and suffix in ['mp4', 'txt']:
            if suffix == 'mp4':
                os.replace(Path(el), os.path.join(path, VIDEO_FOLDER_NAME, Path(el).name))
            else:
                os.replace(Path(el), os.path.join(path, TEXT_FOLDER_NAME, Path(el).name))


print()
sort_files(Path.cwd() / 'Lesson_7')
