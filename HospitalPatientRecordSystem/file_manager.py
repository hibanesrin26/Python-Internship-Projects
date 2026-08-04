import csv
from patient import Patient


class FileManager:

    @staticmethod
    def save_patients(patients, filename="patients.csv"):

        try:
            with open(filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Patient ID",
                    "Patient Name",
                    "Age",
                    "Disease"
                ])

                for patient in patients:
                    writer.writerow([
                        patient.get_patient_id(),
                        patient._name,
                        patient._age,
                        patient.get_disease()
                    ])

            print("Patient data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)


    @staticmethod
    def load_patients(filename="patients.csv"):

        patients = []

        try:
            with open(filename, "r") as file:

                reader = csv.reader(file)
                next(reader)

                for row in reader:

                    patient = Patient(
                        int(row[0]),
                        row[1],
                        int(row[2]),
                        row[3]
                    )

                    patients.append(patient)

        except FileNotFoundError:
            print("No patient data found.")

        except Exception as e:
            print("Error loading file:", e)

        return patients