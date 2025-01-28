def get_number_to_1(number):
    """
    функция возвращает список, который содержит
    все этапы преобразования числа number
    """
    arr = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        arr.append(number)
    return arr


def get_num():
    """
    функция работает до тех пор, пока не будет получено
    подходящее числовое значение
    """
    while True:
        try:
            N = int(input('Введите натуральное число N:\n'))
            if N > 0:
                break
        except ValueError:
            print('Введите число')
    return N


N = get_num()
array = get_number_to_1(N)

print('Последовательность:')
print(*array, sep='->')
print(f'Последовательность содержит {len(array)} членов.')
print(f'Пик последовательности: {max(array)}.')
