from typing import Union, List


class Product:
    def __init__(self, type: str, name: str, price: Union[int, float]) -> None:
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self) -> None:
        self.products = list()
        self.income_store = 0


    def add(self, product: object, amount: int) -> None:
        if not isinstance(product, Product):
            raise ValueError("It does not belong to the class of products")
        store_price = product.price * 1.3
        product = {
            'type': product.type,
            'name': product.name,
            'price': store_price,
            'amount': amount
        }
        self.products.append(product)


    def set_discount(self, indentifier: str, percent: Union[int, float], indentifier_type = 'name') -> None:
        if indentifier_type not in ['name', 'type']:
            raise ValueError("Wrong indentifier")
        for product in self.products:
            if product['name'] or product['type'] == indentifier:
                product['price'] *= 1 - percent / 100


    def sell_product(self, product_name: str, amount: Union[int, float]) -> None:
        for product in self.products:
            if product['name'] == product_name:
                if product['amount'] > amount:
                    product['amount'] -= amount
                    self.income_store += product['price'] * amount
                else:
                    raise ValueError("Not enough product")


    def get_income(self) -> Union[int, float]:
        return self.income_store


    def get_all_products(self) -> List:
        information_of_products = self.products
        return information_of_products


    def get_product_info(self, product_name: str) -> tuple:
        for product in self.products:
            if product['name'] == product_name:
                info_product = (product['name'], product['amount'])
                return info_product


first_product = Product('Sport', 'Football T-Shirt', 100)

second_product = Product('Food', 'Ramen', 1.5)

store = ProductStore()

store.add(first_product, 10)

store.add(second_product, 300)

store.sell_product('Ramen', 10)

assert store.get_product_info('Ramen') == ('Ramen', 290)