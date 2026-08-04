from inventory import Inventory

class InventoryManager:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("No products found.")
        else:
            for product in self.products:
                product.display()
                print("-" * 20)

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_product(self, product_id, quantity):
        product = self.search_product(product_id)

        if product:
            product.set_quantity(quantity)
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        product = self.search_product(product_id)

        if product:
            self.products.remove(product)
            print("Product deleted successfully.")
        else:
            print("Product not found.")