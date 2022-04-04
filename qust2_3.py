while True:
    season = {'Winter': (12, 1, 2),
              'Summer': (6, 7, 8),
              'Spring': (3, 4, 5),
              'Autumn': (9, 10, 11)
              }
    chois_inp = int(input('Введите искомый месяц(при вводе неверного месяца произойдет выход): '))
    if chois_inp >= 13:
        break
    for i in season.keys():
        if chois_inp in season[i]:
            print(i)
