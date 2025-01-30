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


def print_matrix(matrix):
    """
    функция для вывода матрицы на консоль
    """
    for row in matrix.tolist():
        print(*row)


N = get_num()

matrix_A = get_random_matrix(N)

print('Сгенерированная матрица: ')
print_matrix(matrix_A)

min_sum = min(matrix_A.sum(axis=0))

bool_arr = np.apply_along_axis(lambda x: x.sum() == min_sum, axis=0, arr=matrix_A)

indexes = np.argwhere(bool_arr == True)

print('Столбцы с минимальной суммой чисел: ')
for i in indexes:
    print(*i + 1, '- й столбец')
