'''Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноимённых pickle файлов.'''

import json
import pickle

source_data_file = 'update.txt'
target_data_file = 'task_4.txt'


def convert_json_to_pickle(source_file, target_file):
    with open(source_file, 'r', encoding='utf-8') as sf:
        data_j = json.load(sf)
    with open(target_file, 'wb') as tf:
        pickle.dump(data_j, tf)


def main():
    convert_json_to_pickle(source_data_file, target_data_file)


if __name__ == '__main__':
    main()
