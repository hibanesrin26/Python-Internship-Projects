from patient import Patient
from patient_manager import PatientManager
from file_manager import FileManager


manager = PatientManager()

# Load existing patient records
manager.patients = FileManager.load_patients()


while True:

    print("\n===== Hospital Patient Record System =====")
    print("1. Register Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Update Patient Disease")
    print("5. Delete Patient")
    print("6. Save Patients")
    print("7. Exit")


    choice = input("Enter your choice: ")


    try:

        if choice == "1":

            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            disease = input("Enter Disease: ")

            patient = Patient(
                patient_id,
                name,
                age,
                disease
            )

            manager.add_patient(patient)

            print("Patient registered successfully.")


        elif choice == "2":

            manager.display_patients()


        elif choice == "3":

            patient_id = int(input("Enter Patient ID to search: "))

            patient = manager.search_patient(patient_id)

            if patient:
                patient.display()
            else:
                print("Patient not found.")


        elif choice == "4":

            patient_id = int(input("Enter Patient ID: "))
            disease = input("Enter New Disease: ")

            manager.update_patient(
                patient_id,
                disease
            )


        elif choice == "5":

            patient_id = int(input("Enter Patient ID: "))

            manager.delete_patient(patient_id)


        elif choice == "6":

            FileManager.save_patients(
                manager.patients
            )


        elif choice == "7":

            FileManager.save_patients(
                manager.patients
            )

            print("Thank you for using Hospital Patient Record System.")
            break


        else:

            print("Invalid choice.")


    except ValueError:

        print("Please enter valid input.")

    except Exception as e:

        print("Error:", e)