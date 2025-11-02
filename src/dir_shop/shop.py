from src.dir_base.item import ItemShop

class Shop:
    def __init__(self):
        self.storage = {}

    def __repr__(self):
        return repr(self.storage)

    def get_items(self, category_search, name_item_search):
        return self.storage.setdefault(category_search, {}).setdefault(
            name_item_search, []
        )

    def add_item(self, item):
        """Метод добавление товара в хранилище магазина"""
        if isinstance(item, ItemShop):
            category = item.category  # вытаскиваем категорию товара
            name_item = item.item_name  # вытаскиваем название товара

            self.get_items(category, name_item).append(item)
        else:
            print("Ошибка добавление товара, проверьте тип объекта.")

    def remove_item(self, category, name_item, id_item):
        for item in self.get_items(category, name_item):
            print(item)

    def search_item(self, category, name_item, id_item):
        for item in self.get_items(category, name_item):
            if item.id == id_item:
                return item
        else:
            print("Такого товара нет")


