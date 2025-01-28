try:
    with open(input('Введите имя файла:\n'), 'r', encoding='UTF-8') as file:
        data = [i.strip() for i in file.readlines()]
except FileNotFoundError:
    print('Файл с таким именем не был найден.')
    exit()

new_data = ''.join(data).lower()

if len(new_data) == 0:
    print('Файл пустой.')
    exit()

chars = set(new_data)

with open('res_new.txt', 'w', encoding='UTF-8') as file_output:
    for char in chars:
        print(f'{char}: {new_data.count(char)}', file=file_output)
