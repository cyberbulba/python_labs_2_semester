import numpy as np


def get_num():
    """
    функция работает до тех пор, пока не будет получено
    подходящее числовое значение
    """
    while True:
        try:
            N = int(input('Введите натуральное число N (размер квадратной матрицы):\n'))
            if N > 0:
                break
        except ValueError:
            print('Введите число')
    return N


def get_random_matrix(N):
    """
    функция создаёт матрицу N * N,
    заполненную случайными числами и возвращает её
    """
    rand_arr = np.random.randint(1, 101, N * N)
    arr = rand_arr.reshape(N, N)
    return arr


def get_new_matrix(matrix_1, matrix_2, operation):
    """
    функция, возвращающая матрицу, полученную применением
    операции operation к каждому её значению, состоящую из булевых значений
    """
    if operation == '>':
        return matrix_1 > matrix_2
    elif operation == '<':
        return matrix_1 < matrix_2
    return matrix_1 == matrix_2


def print_matrix(matrix):
    """
    функция для вывода матрицы на консоль
    """
    for row in matrix.tolist():
        print(*row)


N = get_num()

matrix_A = get_random_matrix(N)
matrix_B = get_random_matrix(N)

print('Результирующая матрица для оператора ">": ')
print_matrix(np.array(get_new_matrix(matrix_A, matrix_B, '>')))

print('Результирующая матрица для оператора "<": ')
print_matrix(np.array(get_new_matrix(matrix_A, matrix_B, '<')))

print('Результирующая матрица для оператора "=": ')
print_matrix(np.array(get_new_matrix(matrix_A, matrix_B, '=')))
