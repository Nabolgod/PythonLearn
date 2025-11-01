class Shop:
    def __init__(self):
        self.shop = {}

    def __repr__(self):
        return str(self.shop)

    def add_item(self, item):
        self.shop.setdefault(item.category, {}).setdefault(item.item_name, []).append(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def search(self):
        pass

    def editing(self):
        pass

    def delete(self):
        pass

    def read_file(self, filename):
        pass
