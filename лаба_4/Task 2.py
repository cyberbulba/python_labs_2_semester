import os
import shutil


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


archive = 'folder_with_file_and_photos.zip'
new_path = 'unpacked_folder_with_file_and_photos'
shutil.unpack_archive(archive, new_path)

paths = os.listdir(new_path)

paths = [os.path.join(new_path, path) for path in paths]

paths = get_full_path_list(paths)

print(f'Суммарный вес всех файлов: {sum(list(map(lambda x: os.path.getsize(x), paths)))} байт.')
