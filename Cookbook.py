from pprint import pprint


def get_cook_book(file_name):
    """
    Принимает и читает список рецептов из файла в формате:
    Название блюда
    Количество ингредиентов в блюде
    Название ингредиента | Количество | Единица измерения
    Название ингредиента | Количество | Единица измерения
    ...
    Получает словарь в формате:
    {Название блюда: [{'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    {'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    ...],
    Название блюда: [{'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    {'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    ...],
    ...}
    """
    cook_book = {}
    with open(file_name, encoding='utf8') as file:
        for line in file:
            dish = line.strip()
            if dish:
                cook_book[dish] = []
                count = int(file.readline())
                for i in range(count):
                    items = file.readline().strip().split(' | ')
                    temp_dict = {'ingredient name': items[0],
                                 'quantity': items[1],
                                 'measure': items[2]}
                    cook_book[dish].append(temp_dict)
            else:
                return cook_book
            file.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, persons):
    """
    Принимает cook_book, список блюд  и количество персон
    Выводит словарь с названиями ингредиентов и их необходимым количеством
    """
    shop_list = {}
    try:
        for dish in dishes:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient name'] not in shop_list:
                    shop_list[ingredient['ingredient name']] = {'quantity': int(ingredient['quantity']) * persons,
                                                                'measure': ingredient['measure']}
                else:
                    shop_list[ingredient['ingredient name']]['quantity'] += (int(ingredient['quantity']) * persons)
        print(f'Для приготовления блюд на {persons} человек необходимо купить:')
        pprint(shop_list)
    except KeyError:
        print('Вы ошиблись в названии блюда, проверьте ввод.')


def request(file_name):
    """
     Принимает файл в формате:
     Название блюда
     Количество ингредиентов в блюде
     Название ингредиента | Количество | Единица измерения
     Название ингредиента | Количество | Единица измерения
     ...
     Выводит названия блюд из файла
     Запрашивает названия блюд и количество персон, для подсчёта ингридиентов
     Выводит словарь необходимых ингридиентов и их количество
     """
    cook_book = get_cook_book(file_name)
    print('Список блюд, для которых имеются рецепты:')
    for dish_name in cook_book.keys():
        print(dish_name)

    raw_list = input('Введите названия блюд через запятую: ').split(',')
    processed_list = []
    for dish in raw_list:
        processed_list.append(dish.strip().capitalize())

    person_count = 1
    persons = input('Введите количество персон: ')
    try:
        person_count = int(persons)
    except ValueError:
        print('В "количество персон" нужно записать число.')

    get_shop_list_by_dishes(cook_book, processed_list, person_count)


request('recipes.txt')
