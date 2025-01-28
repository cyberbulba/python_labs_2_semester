import re

first_str = input('Введите слова, разделяя их точкой с запятой:\n').split(';')

if len(first_str) != 10:
    print('Вы ввели не 10 слов.')
    exit()

check_str = input('Введите подстроку для проверки:\n')
length = len(check_str)

pattern = r'^' + check_str

flag_slovo = 0
print('Слова, начинающиеся с введёной подстроки:')
for slovo in first_str:
    if re.match(pattern, slovo):
        print(slovo, end=' ')
        flag_slovo = 1

if not flag_slovo:
    print('таких слов нет')
