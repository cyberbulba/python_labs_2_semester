import os


def get_full_paths_list(paths):
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
        if flag == 1:
            break
    return paths


def get_imports(py_file):
    """
    функция открывает файл и возвращает список из строк, которые начинаются с
    from ... import ... или import ...
    """
    with open(py_file, 'r', encoding='UTF-8') as file:
        arr = [i.strip() for i in file.readlines()]
    imports_arr = list(filter(lambda s: s.startswith('from ') or s.startswith('import '), arr))
    return imports_arr


def create_dict_modules(import_res):
    """
    функция, которая возвращает словарь, содержащий пару модуль: список функций,
    созданный на основе списка import res
    """
    key_s = {i[0] for i in import_res}
    dict_modules = {key: [] for key in key_s}
    for key in dict_modules:
        for module in import_res:
            if key in module:
                dict_modules[key].extend(module[1:])
    return dict_modules


def print_dict_modules(dict_modules):
    """
    функция, которая выводит содержимое модулей, хранящееся в словаре (значения словаря)
    """
    for key, values in dict_modules.items():
        print(f'from {key} import ', end='')
        values = list(map(lambda x: ''.join(x.split(',')), values))
        print(*values, sep=', ')


path_name = 'imports'
paths = [os.path.join(path_name, path) for path in os.listdir(path_name)]

paths = get_full_paths_list(paths)

py_files = list(filter(lambda x: os.path.splitext(x)[1] == '.py', paths))

import_res = []
for py_file in py_files:
    import_res.extend(get_imports(py_file))

import_res = [i.split() for i in import_res]
for module in import_res:
    if 'from' in module:
        module.remove('from')
    module.remove('import')

for module in import_res:
    if len(module) == 1:
        print(f'import {module[0]}')
        import_res.remove(module)

dict_modules = create_dict_modules(import_res)

print_dict_modules(dict_modules)
