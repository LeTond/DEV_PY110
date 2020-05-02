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
    matrix = np.zeros((1, n + 1, n + 1), dtype=str)
    for i in range(0, n + 1, 1):
        matrix[0][i][0] = i
    for j in range(0, n + 1, 1):
        matrix[0][0][j] = j
    for i in range(1, n + 1, 1):
        for j in range(1, n + 1):
            matrix[0][i][j] = '_'
    print(matrix, end='\n')
    return matrix

# Условие победы
def condition_func(matrix, n):
    for j in range(1, n + 1):
        if all(matrix[0][i][i] == simbol for i in range(1, n + 1)) \
                or all(matrix[0][i][j] == simbol for i in range(1, n + 1)) \
                or all(matrix[0][j][i] == simbol for i in range(1, n + 1)) \
                or all(matrix[0][i][n + 1 - i] == simbol for i in range(1, n + 1)):
            status = "over"
            return status

# Обработка ошибок при введении координат поля
def digit_exeption(s, d, matrix):
    try:
        if matrix[0][int(s)][int(d)] == 'X' or matrix[0][int(s)][int(d)] == 'O':
            print("*****Это поле уже занято, введите координаты другого поля: ")
            s = input(f"Введите номер строки от 1 до {n}: ")
            d = input(f"Введите номер столбцаот 1 до {n}: ")
            return digit_exeption(s, d, matrix)
    except:
        print("*****Вы ввели некорректные числа, введите правильные: ")
        s = input(f"Введите номер строки от 1 до {n}: ")
        d = input(f"Введите номер столбцаот 1 до {n}: ")
        return digit_exeption(s, d, matrix)
    else:
        matrix[0, int(s), int(d)] = simbol

matrix = ZeroX_Field(n)
if_exit = condition_func(matrix, n)

# Тело игры
while status == "game":
    if counter % 2 == 0:
        simbol = 'X'
    elif counter % 2 != 0:
        simbol = 'O'

    s = input(f"Ход игрока {simbol}-er \nВведите номер строки от 1 до {n}: ")
    d = input(f"Введите номер столбцаот 1 до {n}: ")

    digit_exeption(s, d, matrix)    # Проверка корректности хода

    print(matrix, end='\n')
    counter += 1
    if counter >= n:
        condition_func(matrix, n)       # Проверка победного состояния

    if condition_func(matrix, n) == 'over':
        print(f"-----------Победа игрока {simbol}-er-----------")
        break
    elif counter >= n ** 2:
        print("------------Ничья-----------")
        break

