'''Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
варианты и выведите 4 успешных расстановки.'''

from random import randint
from task_2 import checking_placement_of_queens as queens


def queens_rnd():
    coordinate_x = []
    coordinate_y = []
    for _ in range(8):
        coordinate_x.append(randint(1, 8))
        coordinate_y.append(randint(1, 8))
    return coordinate_x, coordinate_y


def queens_result():
    coor_x, coor_y = [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]
    result_list = []
    for _ in range(4):
        while not queens(coor_x, coor_y):
            coor_x, coor_y = queens_rnd()
        result_list.append([coor_x, coor_y])
    return result_list


if __name__ == '__main__':
    print(queens_result())
