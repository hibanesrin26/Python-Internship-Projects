from rental import Rental
from rental_manager import RentalManager
from file_manager import FileManager


manager = RentalManager()

# Load existing rental records
manager.rentals = FileManager.load_rentals()


while True:

    print("\n===== Vehicle Rental Management System =====")
    print("1. Add Rental")
    print("2. Display Rentals")
    print("3. Search Rental")
    print("4. Update Rental Days")
    print("5. Delete Rental")
    print("6. Save Rentals")
    print("7. Exit")


    choice = input("Enter your choice: ")


    try:

        if choice == "1":

            vehicle_id = int(input("Enter Vehicle ID: "))
            brand = input("Enter Vehicle Brand: ")
            model = input("Enter Vehicle Model: ")
            rent = float(input("Enter Rent Per Day: "))
            days = int(input("Enter Number of Days: "))


            rental = Rental(
                vehicle_id,
                brand,
                model,
                rent,
                days
            )

            manager.add_rental(rental)

            print("Vehicle rental added successfully.")



        elif choice == "2":

            manager.display_rentals()



        elif choice == "3":

            vehicle_id = int(input("Enter Vehicle ID to search: "))

            rental = manager.search_rental(vehicle_id)


            if rental:
                rental.display()

            else:
                print("Rental not found.")



        elif choice == "4":

            vehicle_id = int(input("Enter Vehicle ID: "))
            days = int(input("Enter New Rental Days: "))

            manager.update_rental_days(
                vehicle_id,
                days
            )



        elif choice == "5":

            vehicle_id = int(input("Enter Vehicle ID: "))

            manager.delete_rental(vehicle_id)



        elif choice == "6":

            FileManager.save_rentals(
                manager.rentals
            )



        elif choice == "7":

            FileManager.save_rentals(
                manager.rentals
            )

            print("Thank you for using Vehicle Rental Management System.")

            break



        else:

            print("Invalid choice.")


    except ValueError:

        print("Please enter valid input.")


    except Exception as e:

        print("Error:", e)