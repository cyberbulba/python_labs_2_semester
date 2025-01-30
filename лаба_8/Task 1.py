import pandas as pd


def get_num():
    """
    функция работает до тех пор, пока не будет получено
    подходящее числовое значение
    """
    while True:
        try:
            N = int(input())
            if N > 0:
                break
        except ValueError:
            print('Введите число')
    return N


def get_country(df):
    """
    функция запрашивает у ползователя название страны до тех пор,
    пока не будет получено существующее название страны,
    после этого возвращает его
    """
    while True:
        name = input('Введите название страны: \n')
        if name in df['country'].values:
            break
        print('Такой страны нет, введите другую')
    return name


def task_a(df):
    """
    функция выводит на консоль название самого/самых высокого и низкого зданий из DataFrame
    """
    print('Самые высокие здания: ')
    print(*df.nlargest(5, 'height_m')['name'], sep='\n')

    print('Самые низкие здания: ')
    print(*df.nsmallest(5, 'height_m')['name'], sep='\n')


def task_b(df):
    """
    функция выводит на консоль минимальную, максимальную, среднюю и
    среднюю медианную высоту зданий из DataFrame
    """
    height_values = df['height_m']
    print(f'Максимальная высота здания: {height_values.min()}')
    print(f'Минимальная высота здания: {height_values.max()}')
    print(f'Средняя высота здания: {height_values.mean()}')
    print(f'Среднее медианное значение высоты зданий: {height_values.median()}')


def task_c(df):
    """
    функция выводит на консоль количество стран, упомянутых в DataFrame
    """
    print(f'В файле упомянуто {df['country'].nunique()} стран')


def task_d(df):
    """
    функция выводит на консоль названия самых старых и новых зданий из DataFrame
    """
    min_year = df['year_built'].min()
    max_year = df['year_built'].max()

    print('Самое старое здание/здания: ')
    min_year_buildings = df[df['year_built'] == min_year]
    print(*min_year_buildings['name'], sep='\n')

    print('Самое новое здание/здания: ')
    max_year_buildings = df[df['year_built'] == max_year]
    print(*max_year_buildings['name'], sep='\n')


def task_e(df):
    """
    функция выводит на консоль новый DataFrame, состоящий из зданий из старого DataFrame,
    количество этажей которых превышает введённое пользователем значение
    """
    print('Введите число, больше которого будет количество этажей: ')
    n_floors = get_num()
    new_df = df[df['floors_above'] > n_floors]
    print(f'DataFrame, который содержит информацию о зданиях, в которых больше {n_floors} этажей: ')
    print(new_df)


def task_f(df):
    """
    функция выводит на консоль имена зданий из DataFrame, год постройки которых совпадает с
    годом, введённым пользователем
    """
    print('Введите год постройки зданий: ')
    year_input = get_num()
    year_input_buildings = df[df['year_built'] == year_input]
    print(f'Здания, построенные в {year_input} году: ')
    if len(year_input_buildings) == 0:
        print('Таких зданий нет')
    print(*year_input_buildings['name'], sep='\n')


def task_g(df):
    """
    функция выводит на консоль количество зданий из DataFrame,
    которые располагаются в введённой пользователем стране
    """
    country = get_country(df)
    builds_in_country = df[df['country'] == country]
    print(f'В стране {country} находится {len(builds_in_country)} зданий из списка')


try:
    dataframe = pd.read_csv('data_tallest_buildings.csv')
except FileNotFoundError:
    print('Файл не найден')
    exit()

task_a(dataframe)
task_b(dataframe)
task_c(dataframe)
task_d(dataframe)
task_e(dataframe)
task_f(dataframe)
task_g(dataframe)
