from inventory import Inventory
from inventory_manager import InventoryManager
from file_manager import FileManager

manager = InventoryManager()

# Load existing products
manager.products = FileManager.load_products()

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Product Quantity")
    print("5. Delete Product")
    print("6. Save Products")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))

            product = Inventory(product_id, name, price, quantity)
            manager.add_product(product)
            print("Product added successfully.")

        elif choice == "2":
            manager.display_products()

        elif choice == "3":
            product_id = int(input("Enter Product ID to search: "))
            product = manager.search_product(product_id)

            if product:
                product.display()
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter New Quantity: "))
            manager.update_product(product_id, quantity)

        elif choice == "5":
            product_id = int(input("Enter Product ID: "))
            manager.delete_product(product_id)

        elif choice == "6":
            FileManager.save_products(manager.products)

        elif choice == "7":
            FileManager.save_products(manager.products)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print("Error:", e)