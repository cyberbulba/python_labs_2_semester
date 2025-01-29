import os
import re


def get_full_path_list(paths):
    """
    функция, которая проходит по всем директориям, содержащимся
    в списке paths и возвращает полный список файлов
    """
    while True:
        flag = 1
        for path in paths:
            if os.path.isdir(path):
                paths.extend([os.path.join(path, i) for i in os.listdir(path)])
                paths.remove(path)
                flag = 0
        if flag:
            break
    return paths


def get_ext():
    """
    функция запрашивает у пользователя строку до тех пор,
    пока она не будет являться расширением
    """
    pattern_ext = r'^\.[a-zA-Z]+$'
    while True:
        ext = input('Введите расширение файлов: ')
        if re.fullmatch(pattern_ext, ext):
            break
    return ext


path_name = 'folder_with_file_and_photos'
paths = os.listdir(path_name)

paths = [os.path.join(path_name, path) for path in paths]

paths = get_full_path_list(paths)

ext = get_ext()

files_with_this_ext = list(filter(lambda x: os.path.splitext(x)[1] == ext, paths))
files = [os.path.split(file)[1] for file in files_with_this_ext]
print(f'Файлы с расширением {ext}: ', end='')
print(*files, sep=', ', end='.')
