import os
import shutil


def get_directory_name():
    """
    функция запрашивает у пользователя корректное имя директории и возвращает его
    """
    while True:
        directory = input()
        if os.path.exists(directory):
            break
        print('Такой директории нет, введите заново.')
    return directory


print('Введите путь до директории src: ')
src = get_directory_name()

print('Введите путь до директории dst: ')
dst = get_directory_name()

if src == dst:
    print('Имена директорий совпадают.')
    exit()

paths = [os.path.join(src, path) for path in os.listdir(src)]

files = list(filter(lambda x: os.path.isfile(x), paths))

photos = list(filter(lambda x: os.path.splitext(x)[1] in ['.png', '.jpg', '.jpeg'], files))

for photo in photos:
    shutil.move(photo, dst)

shutil.make_archive('ArchivedMyDirectory', 'zip', dst)
