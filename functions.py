from dao.request import Request
from dao.shop import Shop
from dao.store import Store


def check_input(user_input):
    """Небольшая проверка ввода пользователя"""
    # начало небольшой проверки ввода пользователя #
    if user_input == 'хватит':
        print('спасибо, что воспользовались услугами нашей службы доставки')
        exit()
    if Request(user_input).get_to() is None:
        print('Непонятен пункт назначения')
        exit()
    if Request(user_input).get_from() is None:
        print('Непонятен пункт отправления')
        exit()
    if Request(user_input).get_amount() is None:
        print('Неясно количество товара')
        exit()
    if Request(user_input).get_product() is None:
        print('Непонятен пункт отправления')
        exit()
    # завершение небольшой проверки ввода пользователя #


def to_shop(product, amount):
    """Доставка товаров со склада в магазин"""
    shop = Shop()
    store = Store()
    store.remove(product, amount)
    print(f'Курьер взял {amount} {product} со склада')
    print(f'Курьер везёт {amount} {product} в магазин')
    shop.add(product, amount)
    print(f'Курьер доставил {amount} {product} в магазин')


def to_store(amount, product):
    """Доставка товаров из магазина на склад"""
    shop = Shop()
    store = Store()
    shop.remove(product, amount)
    print(f'Курьер взял {amount} {product} из магазина')
    print(f'Курьер везёт {amount} {product} на склад')
    store.add(product, amount)
    print(f'Курьер доставил {amount} {product} на склад')


def print_store():
    """Наличие товаров на складе"""
    store = Store()
    data = store.get_items()
    print('На складе хранится:')
    for i in data:
        print(f'{data[i]} {i}')
    print('')


def print_shop():
    """Наличие товаров в магазине"""
    shop = Shop()
    data = shop.get_items()
    print('В магазине хранятся:')
    for i in data:
        print(f'{data[i]} {i}')
