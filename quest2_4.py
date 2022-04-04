for i, word in enumerate(input('Введите слово: ').split(' '), start=1):
    print(f'{i}.', word[:10].title())
