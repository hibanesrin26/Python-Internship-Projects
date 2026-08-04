class RentalManager:

    def __init__(self):
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def display_rentals(self):

        if not self.rentals:
            print("No rental records found.")

        else:
            for rental in self.rentals:
                rental.display()
                print("-" * 20)


    def search_rental(self, vehicle_id):

        for rental in self.rentals:

            if rental.get_vehicle_id() == vehicle_id:
                return rental

        return None


    def update_rental_days(self, vehicle_id, days):

        rental = self.search_rental(vehicle_id)

        if rental:

            rental.set_days(days)
            print("Rental details updated successfully.")

        else:
            print("Rental not found.")


    def delete_rental(self, vehicle_id):

        rental = self.search_rental(vehicle_id)

        if rental:

            self.rentals.remove(rental)
            print("Rental deleted successfully.")

        else:
            print("Rental not found.")