from typing import Union, List


class Product:
    def __init__(self, type: str, name: str, price: Union[int, float]) -> None:
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self) -> None:
        self.products = list()
        self.__income_store = 0


    def add(self, product: object, amount: int) -> None:
        if not isinstance(product, Product):
            raise ValueError("It does not belong to the class of products")
        self.products.append({'product': product, 'amount': amount, 'price_store': product.price * 1.3})


    def set_discount(self, indentifier: str, percent: Union[int, float], indentifier_type = 'name') -> None:
        if indentifier_type not in ['name', 'type']:
            raise ValueError("Wrong indentifier")
        for item in self.products:
            if item['product'].name or item['product'].type == indentifier:
                item['price_store'] *= 1 - percent / 100


    def sell_product(self, product_name: str, amount: Union[int, float]) -> None:
        for item in self.products:
            if item['product'].name == product_name:
                if item['amount'] > amount:
                    item['amount'] -= amount
                    self.__income_store += item['price_store'] * amount
                else:
                    raise ValueError("Not enough product")


    def get_income(self) -> Union[int, float]:
        return self.__income_store


    def get_all_products(self) -> List:
        if self.products is []:
            raise ValueError("Product list is empty")
        information_of_products = [(item['product'].name, item['product'].type, item['amount'], item['price_store'])
                                   for item in self.products]
        return information_of_products


    def get_product_info(self, product_name: str) -> tuple:
        for item in self.products:
            if item['product'].name == product_name:
                info_product = (item['product'].name, item['amount'])
                return info_product
        raise ValueError("Product not found")


first_product = Product('Sport', 'Football T-Shirt', 100)
second_product = Product('Food', 'Ramen', 1.5)

store = ProductStore()

store.add(first_product, 10)
store.add(second_product, 300)
store.sell_product('Ramen', 10)

assert store.get_product_info('Ramen') == ('Ramen', 290)