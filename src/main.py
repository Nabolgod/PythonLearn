from src.dir_laptop.laptop import Laptop
from src.dir_shop.shop import Shop

if __name__ == "__main__":
    shop = Shop()
    shop.add_item(Laptop())
    shop.add_item(Laptop())

    print(shop)
