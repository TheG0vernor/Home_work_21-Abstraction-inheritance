class Request:
    def __init__(self, string):
        self._from = None  # откуда
        self._to = None  # куда
        self._amount = None  # количество
        self._product = None  # наименование
        self.string = string  # поступающая строка
        try:  # обработка поступающей строки
            data = self.string.split(' ')
            for i in data:
                if i.isdigit():  # определить число в строке
                    self._amount = (int(i))  # назначить количество
                    self._product = (data[data.index(i) + 1])  # назначить продукцию
                if i.lower() == 'из' or i.lower() == 'со':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self._from = 'склад'  # назначить пункт отправления
                        self._to = 'магазин'  # назначить пункт назначения
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self._to = 'магазин'  # назначить пункт отправления
                        self._from = 'склад'  # назначить пункт назначения

                elif i.lower() == 'в' or i.lower() == 'на':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self._to = 'склад'  # назначить пункт назначения
                        self._from = 'магазин'  # назначить пункт отправления
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self._from = 'склад'  # назначить пункт отправления
                        self._to = 'магазин'  # назначить пункт назначения
        except Exception as e:
            raise print(e, 'ошибка ввода данных')

    @property
    def from_(self):  # вернёт пункт отправление
        return self._from

    @from_.setter
    def from_(self, new_from):  # назначит пункт отправления
        self._from = new_from

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, new_to):
        self._to = new_to

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, new_product):
        self._product = new_product
