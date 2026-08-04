import csv


class FileManager:


    @staticmethod
    def save_registrations(registrations, filename="registrations.csv"):

        try:

            with open(filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Student ID",
                    "Course ID"
                ])


                for registration in registrations:

                    writer.writerow([
                        registration[0],
                        registration[1]
                    ])


            print("Registration data saved successfully.")


        except Exception as e:

            print("Error saving file:", e)



    @staticmethod
    def load_registrations(filename="registrations.csv"):

        registrations = []


        try:

            with open(filename, "r") as file:

                reader = csv.reader(file)

                next(reader)


                for row in reader:

                    registrations.append(
                        (
                            int(row[0]),
                            int(row[1])
                        )
                    )


        except FileNotFoundError:

            print("No registration data found.")


        except Exception as e:

            print("Error loading file:", e)


        return registrations