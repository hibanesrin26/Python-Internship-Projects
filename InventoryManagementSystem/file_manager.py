import csv
from inventory import Inventory

class FileManager:

    @staticmethod
    def save_products(products, filename="products.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["Product ID", "Product Name", "Price", "Quantity"])

                for product in products:
                    writer.writerow([
                        product.get_product_id(),
                        product._name,
                        product._price,
                        product.get_quantity()
                    ])

            print("Product data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

    @staticmethod
    def load_products(filename="products.csv"):
        products = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    product = Inventory(
                        int(row[0]),
                        row[1],
                        float(row[2]),
                        int(row[3])
                    )
                    products.append(product)

        except FileNotFoundError:
            print("No existing product data found.")

        except Exception as e:
            print("Error loading file:", e)

        return products