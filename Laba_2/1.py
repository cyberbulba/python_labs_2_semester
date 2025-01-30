import json

try:
    with open('animals.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print('Файл не найден.')
    exit()

new_data = data['animals']

birds = list(filter(lambda animal: animal['animal_type'] == 'Bird', new_data))
print('Данные о птицах:')
for bird in birds:
    for key, value in bird.items():
        print(f'{key}: {value}')
    print()

if len(birds) == 0:
    print('Нет сведений о птицах.')

diurnal_animals = len(list(filter(lambda animal: animal['active_time'] == 'Diurnal', new_data)))
print(f'Дневных животных: {diurnal_animals} \n')

weight_animals = sorted(new_data, key=lambda animal: animal['weight_min'])
print('Данные о животном с наименьшим весом:')
for key, value in weight_animals[0].items():
    print(f'{key}: {value}')
