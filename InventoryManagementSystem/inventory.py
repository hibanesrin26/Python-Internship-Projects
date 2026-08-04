from product import Product

class Inventory(Product):

    def __init__(self, product_id, name, price, quantity):
        super().__init__(product_id, name, price)
        self.__quantity = quantity

    def get_product_id(self):
        return self._product_id

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def display(self):
        print(f"Product ID: {self._product_id}")
        print(f"Product Name: {self._name}")
        print(f"Price: {self._price}")
        print(f"Quantity: {self.__quantity}")