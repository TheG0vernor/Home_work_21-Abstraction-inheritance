from abc import ABC

from dao.base import Storage


class Shop(Storage, ABC):
    _items = {'блины': 4, 'вареники': 3}
    _capacity = 13

    @classmethod
    def add(cls, the_name, quantity):  # метод добавит товары на склад магазина
        if cls._capacity >= quantity:
            if the_name in cls._items:
                cls._items[the_name] += quantity
                cls._capacity -= quantity
            else:
                if cls.unique_items_count() < 5:
                    cls._items[the_name] = quantity
                    cls._capacity -= quantity
                else:
                    print('Магазин не принял курьера, поскольку превышен \nлимит хранимых на складе наименований товаров')
                    exit()
        else:
            print('Недостатошно места на складе магазина')
            exit()

    @classmethod
    def remove(cls, the_name, quantity):  # метод изымет товары со склада магазина
        if the_name not in cls._items:
            print(f'Нет такого товара {the_name} в магазине')
            exit()
        elif cls._items.get(the_name) < quantity:
            print(f'Нет такого количества товара {the_name} на складе магазина')
            exit()
        elif cls._capacity + quantity > 100:
            print('Склад магазина заполнен')
            exit()
        elif the_name in cls._items:
            cls._items[the_name] -= quantity
            cls._capacity += quantity
            if cls._items[the_name] == 0:  # удаление наименования товара на складе магазина, если он закончился
                del cls._items[the_name]

    @classmethod
    def get_free_space(cls):  # возвращает свободное пространство на складе магазина
        return cls._capacity

    @classmethod
    def get_items(cls):  # возвращает наименование и количество товаров на складе магазина
        return cls._items

    @classmethod
    def unique_items_count(cls):  # возвращает количество уникальных товаров на складе магазина
        return len(set(cls._items))
