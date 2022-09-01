from dao.request import Request
from functions import check_input, print_store, print_shop, to_store, to_shop, check_input_low

print('Привет и добро пожаловать в мою программу доставки!\n')
user_input = (input(
    'Доставлять можно между складом и магазином. \n'
    'Не забудьте указать количество! И наименование товара. \n'
    'Для начала напишите "начали" или что-нибудь ещё. '
    'Для завершения пришлите "хватит"\n'))
check_input_low(user_input)

while True:
    print_store()  # отображение товара на складах в наличии
    print_shop()
    user_input = (input('\nЧто вам угодно доставить?\n'))
    check_input(user_input)  # проверка ввода пользователя
    to = Request(user_input).get_to()
    from_ = Request(user_input).get_from()  # назначение переменных
    amount = Request(user_input).get_amount()
    product = Request(user_input).get_product()
    if to == 'склад':
        to_store(product=product, amount=amount)
    else:
        to_shop(amount=amount, product=product)
