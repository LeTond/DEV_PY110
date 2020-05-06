'''
Входное задание PY110 Срок заканчивается 29 мая 2020 г., 23: 59
Инструкции До конца курса PY110, а именно до зачетного занятия, необходимо выполнить входное задание.
Оно представляет собой консольное приложение, реализующее игру в крестики - нолики.
В игре должна быть возможность играть двум игрокам.После запроса хода, должна производиться проверка его корректности,
в случае успешности производится проверка, является ли данное состояние победным.
Результатом выполнения должен быть исходные код приложения в любом формате.Файл с раширением.py либо репозиторий на git
'''
import numpy as np

n = 3       # Величина игрового поля (n x n)
counter = 0     # Счетчик ходов
simbol = ""
status = "game"

# Создание игрового поля
def ZeroX_Field(n):
    matrix = np.full((n, n), '_', dtype=str)
    matrix[:, 0] = range(0, n)
    matrix[0, :] = range(0, n)
    print(matrix, end='\n')
    return matrix

# Условие победы
# TODO: убрать for, реализовать проверку через np
def condition_func(matrix, n, simbol):
    matrix2 = np.full((n, 1), simbol, dtype=str)
    if (np.diagonal(matrix) == matrix2).all() \
            or (np.diagonal(np.rot90(matrix)) == matrix2).all():
            # or (matrix.any(axis=0) == matrix2).all():
        status = 'over'
        return status

# Обработка ошибок при введении координат поля
def digit_exeption(s, d, matrix):
    while True:
        try:
            while matrix[int(s)][int(d)] == 'X' \
                    or matrix[int(s)][int(d)] == 'O':
                print("*****Это поле уже занято, введите координаты другого поля: ")
                s = input(f"Введите номер строки от 0 до {n - 1}: ")
                d = input(f"Введите номер столбцаот 0 до {n - 1}: ")
        except:
            print("*****Вы ввели некорректные координаты*****")
            s = input(f"Введите номер строки от 0 до {n-1}: ")
            d = input(f"Введите номер столбцаот 0 до {n-1}: ")
        else:
            matrix[int(s), int(d)] = simbol
            break
matrix = ZeroX_Field(n)

# Тело игры
while status == "game":
    if counter % 2 == 0:
        simbol = 'X'
    elif counter % 2 != 0:
        simbol = 'O'

    s = input(f"Ход игрока {simbol}-er \nВведите номер строки от 0 до {n-1}: ")
    d = input(f"Введите номер столбцаот 0 до {n-1}: ")

    digit_exeption(s, d, matrix)    # Проверка корректности хода

    print(matrix, end='\n')
    counter += 1
    if counter >= n:
        condition_func(matrix, n, simbol)       # Проверка победного состояния

    if condition_func(matrix, n, simbol) == 'over':
        print(f"-----------Победа игрока {simbol}-er-----------")
        break
    elif counter >= n ** 2:
        print("------------Ничья-----------")
        break

