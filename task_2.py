'''Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть
ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''


def checking_placement_of_queens(x, y):
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True

if __name__ == '__main__':
    n = 8
    x = []
    y = []
    for i in range(n):
        coor_x, coor_y = [int(j) for j in input().split()]
        x.append(coor_x)
        y.append(coor_y)
    print(checking_placement_of_queens(x, y))