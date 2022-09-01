from abc import ABC

from dao.base import Storage


class Store(Storage, ABC):
    _items = {'вино': 20, 'хлеб': 15, 'мясо': 12, 'оружие': 3}
    _capacity = 50

    @classmethod
    def add(cls, the_name, quantity):  # метод добавит товары на склад
        if cls._capacity >= quantity:
            if the_name in cls._items:
                cls._items[the_name] += quantity
                cls._capacity -= quantity
            else:
                cls._items[the_name] = quantity
                cls._capacity -= quantity
        else:
            print('Недостатошно места на складе')
            exit()

    @classmethod
    def remove(cls, the_name, quantity):  # метод изымет товары со склада
        if the_name not in cls._items:
            print(f'Нет такого товара {the_name}')
            exit()
        elif cls._items.get(the_name) < quantity:
            print(f'Нет такого количества товара {the_name} на складе')
            exit()
        elif the_name in cls._items:
            cls._items[the_name] -= quantity
            cls._capacity += quantity
            if cls._items[the_name] == 0:  # удаление наименования товара на складе, если он закончился
                del cls._items[the_name]

    @classmethod
    def get_free_space(cls):  # возвращает свободное пространство на складе
        return cls._capacity

    @classmethod
    def get_items(cls):  # возвращает наименование и количество товаров на складе
        return cls._items

    @classmethod
    def unique_items_count(cls):  # возвращает количество уникальных товаров на складе
        return len(set(cls._items))
