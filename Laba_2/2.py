import csv


def get_num():
    """
    функция работает до тех пор, пока не будет получено
    числовое значение
    """
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print('Введите число.')
    return num


with open('countries.csv', 'r', encoding='UTF-8') as file:
    data = csv.DictReader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    countries = [country for country in data if '' not in country.values()]

headers = list(countries[0].keys())

while True:
    print('Введите минимальный показатель дохода:')
    minimum = get_num()
    print('Введите максимальный показатель дохода:')
    maximum = get_num()
    if minimum <= maximum:
        break
    print('Минимум не должен быть больше максимума.')

income_in_range = list(filter(lambda x: minimum <= x['Income'] <= maximum, countries))

with open('countries_1.csv', 'w', encoding='UTF-8', newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=headers)
    writer.writeheader()
    for country in income_in_range:
        writer.writerow(country)

inflation_sorted = sorted(countries, key=lambda x: x['Inflation'])

with open('countries_2.csv', 'w', encoding='UTF-8', newline="") as output_file_new:
    writer = csv.DictWriter(output_file_new, fieldnames=headers)
    writer.writeheader()
    for country in inflation_sorted:
        writer.writerow(country)
