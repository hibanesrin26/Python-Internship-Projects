import csv
from rental import Rental


class FileManager:


    @staticmethod
    def save_rentals(rentals, filename="rentals.csv"):

        try:

            with open(filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Vehicle ID",
                    "Brand",
                    "Model",
                    "Rent Per Day",
                    "Days"
                ])


                for rental in rentals:

                    writer.writerow([
                        rental.get_vehicle_id(),
                        rental._brand,
                        rental._model,
                        rental._rent_per_day,
                        rental.get_days()
                    ])


            print("Rental data saved successfully.")


        except Exception as e:

            print("Error saving file:", e)



    @staticmethod
    def load_rentals(filename="rentals.csv"):

        rentals = []


        try:

            with open(filename, "r") as file:

                reader = csv.reader(file)

                next(reader)


                for row in reader:

                    rental = Rental(
                        int(row[0]),
                        row[1],
                        row[2],
                        float(row[3]),
                        int(row[4])
                    )

                    rentals.append(rental)


        except FileNotFoundError:

            print("No rental data found.")


        except Exception as e:

            print("Error loading file:", e)


        return rentals