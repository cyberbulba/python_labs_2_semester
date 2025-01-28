def get_num():
    """
    функция работает до тех пор, пока не будет получено
    подходящее числовое значение
    """
    while True:
        try:
            N = int(input('Введите число N, больше которого должны быть баллы:\n'))
            break
        except ValueError:
            print('Введите число')
    return N

try:
    with open(input('Введите имя файла:\n'), 'r', encoding='UTF-8') as file:
        data = [i.strip().split() for i in file.readlines()]
except FileNotFoundError:
    print('Файл с таким именем не был найден.')
    exit()

try:
    for person in data:
        person[1] = int(person[1])
except ValueError:
    print('В графе оценки введено не число.')
    exit()

sorted_names = sorted(data, key=lambda name: name[0])
print('Сортировка по именам:')
for name in sorted_names:
    print(*name)

sorted_marks = sorted(data, key=lambda name: name[1])
print('Сортировка по баллам:')
for name in sorted_marks:
    print(*name)

N = get_num()

with open('res.txt', 'w', encoding='UTF-8') as file_output:
    new_data = filter(lambda name: name[1] > N, data)
    for name in new_data:
        print(*name, file=file_output)
