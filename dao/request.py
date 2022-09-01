class Request:
    def __init__(self, string):
        self._from = None  # откуда
        self._to = None  # куда
        self._amount = None  # количество
        self._product = None  # наименование
        self.string = string  # поступающая строка
        try:  # обработка поступающей строки
            _range = range(1, 501)
            list_range = []
            for i in _range:
                list_range.append(str(i))
            data = self.string.split(' ')
            for i in data:
                if i in list_range:
                    self.set_amount(int(i))  # назначить количество
                    self.set_product(data[data.index(i) + 1])  # назначить продукцию
                if i.lower() == 'из' or i.lower() == 'со':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self.set_from('склад')  # назначить пункт отправления
                        self.set_to('магазин')  # назначить пункт назначения
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self.set_from('магазин')  # назначить пункт отправления
                        self.set_to('склад')  # назначить пункт назначения

                elif i.lower() == 'в' or i.lower() == 'на':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self.set_from('магазин')  # назначить пункт отправления
                        self.set_to('склад')  # назначить пункт назначения
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self.set_from('склад')  # назначить пункт отправления
                        self.set_to('магазин')  # назначить пункт назначения
        except Exception as e:
            raise print(e, 'ошибка ввода данных')

    def get_from(self):  # вернёт пункт отправление
        return self._from

    def set_from(self, _from):  # назначит пункт отправления
        self._from = _from

    def get_to(self):
        return self._to

    def set_to(self, new_to):
        self._to = new_to

    def get_amount(self):
        return self._amount

    def set_amount(self, _amount):
        self._amount = _amount

    def get_product(self):
        return self._product

    def set_product(self, _product):
        self._product = _product
