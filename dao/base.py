from abc import ABC, abstractmethod


class Storage(ABC):  # абстрактный класс с методами и полями
    @property
    @abstractmethod
    def _items(self):
        pass

    @property
    @abstractmethod
    def _capacity(self):
        pass

    @abstractmethod
    def add(self, the_name, quantity):
        pass

    @abstractmethod
    def remove(self, the_name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def unique_items_count(self):
        pass
