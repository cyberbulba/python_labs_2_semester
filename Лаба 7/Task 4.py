import numpy as np

data_arr = np.genfromtxt('udemy_courses.csv', delimiter=',', skip_header=1, dtype=None, encoding='UTF-8')

prices = data_arr['f1']
print(f'Средняя цена за курс: {sum(prices)/len(prices)}')

subscribers = data_arr['f2']
print(f'Минимальное число подписчиков: {min(subscribers)}')

timing = data_arr['f5']
print(f'Максимальная продолжительность курса: {max(timing)}')

set_levels, counts = np.unique(data_arr['f4'], return_counts=True)

arr_levels = list(zip(set_levels, counts))
arr_levels = sorted(arr_levels, key=lambda level: level[1], reverse=True)

print('Больше всего курсов на уровне/уровнях: ', end='')
for level in arr_levels:
    if level[1] == arr_levels[0][1]:
        print(level[0])
