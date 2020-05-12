"""
Входное задание PY110 Срок заканчивается 29 мая 2020 г., 23: 59
Инструкции До конца курса PY110, а именно до зачетного занятия, необходимо выполнить входное задание.
Оно представляет собой консольное приложение, реализующее игру в крестики - нолики.
В игре должна быть возможность играть двум игрокам.После запроса хода, должна производиться проверка его корректности,
в случае успешности производится проверка, является ли данное состояние победным.
Результатом выполнения должен быть исходные код приложения в любом формате.Файл с раширением.py либо репозиторий на git
"""

import numpy as np

n = 3  # Величина игрового поля (n x n)
counter = 0  # Счетчик ходов
simbol = ""
status = "game"


# Создание игрового поля
def zero_x_field(n):
    matrix = np.full((n, n), '_', dtype=str)
    matrix[:, 0] = range(0, n)
    matrix[0, :] = range(0, n)
    print(matrix, end='\n')
    return matrix


# Условие победы
def condition_func(matrix, simbol):
    if ((np.diagonal(matrix) == simbol).all()).any() \
            or ((np.diagonal(np.rot90(matrix)) == simbol).all()).any() \
            or (matrix == simbol).all(axis=0).any() \
            or (matrix == simbol).all(axis=1).any():
        status = 'over'
        return status


# Обработка ошибок при введении координат поля
def digit_exeption(matrix):
    while True:
        try:
            s = input(f"Введите номер строки от 0 до {n - 1}: ")
            d = input(f"Введите номер столбца от 0 до {n - 1}: ")
            if matrix[int(s)][int(d)] != 'X' \
                    and matrix[int(s)][int(d)] != 'O':
                matrix[int(s), int(d)] = simbol
                break
            else:
                print("*****Это поле уже занято, введите координаты другого поля: ")
        except ValueError:
            print("*****Вы ввели некорректные координаты*****")
        except IndexError:
            print("*****Вы ввели некорректные координаты*****")


matrix = zero_x_field(n)

# Тело игры
while status:
    if counter % 2 == 0:
        simbol = 'X'
    elif counter % 2 != 0:
        simbol = 'O'

    print(f"Ход игрока {simbol}-er")
    digit_exeption(matrix)  # Проверка корректности хода

    print(matrix, end='\n')
    counter += 1
    if counter >= n:
        condition_func(matrix, simbol)  # Проверка победного состояния

    if condition_func(matrix, simbol) == 'over':
        print(f"-----------Победа игрока {simbol}-er-----------")
        break
    elif counter >= n ** 2:
        print("------------Ничья-----------")
        break
