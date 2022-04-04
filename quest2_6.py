lst_null = []
analitic_dict = {'Название': [],
               'Цена': [],
               'Кол-во': [],
               'Ед.измерения': []
                 }
num = 1

while True:
    name = input('Введи название: ')
    price = int(input('Введи цену: '))
    stock = int(input('Введи колличество: '))
    name_2 = input('Введи еденицы измерения: ')

    dc_null = {'Название': name,
               'Цена': price,
               'Кол-во': stock,
               'Ед.измерения': name_2
               }
    tp_null = (num, dc_null)
    lst_null.append(tp_null)
    for key, values in dc_null.items():
        i = analitic_dict.get(key)
        if values in i:
            continue
        i.append(values)
        continue
    num += 1
    exit_answer = input('Продолжаем ввод данных?: ').lower()
    if exit_answer == 'нет':
        break
print(analitic_dict)