import numpy as np

try:
    size = np.loadtxt('Linear_system.txt', dtype=None,  delimiter=' ', max_rows=1)
    system = np.loadtxt('Linear_system.txt', dtype=None, delimiter=' ', skiprows=1)
except FileNotFoundError:
    print('Файла нет в директории')
    exit()

if size == 0:
    print('Система пустая')
    exit()

b_coef = system[-1]
system = system[:-1]

if len(system) != size or len(system[0]) != size:
    print('Размер матрицы неправильный (она должна быть квадратной)')
    exit()

try:
    x = np.linalg.solve(system, b_coef)
except np.linalg.LinAlgError as exception:
    print(f'Произошла ошибка при решении: {exception}')
    exit()

print('Решения системы: ')
number = 1
for answer in x:
    print(f'x{number} = {round(answer, 2)}')
    number += 1
