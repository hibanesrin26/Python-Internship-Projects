class PatientManager:

    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients:
                patient.display()
                print("-" * 20)

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.get_patient_id() == patient_id:
                return patient
        return None

    def update_patient(self, patient_id, disease):
        patient = self.search_patient(patient_id)

        if patient:
            patient.set_disease(disease)
            print("Patient record updated successfully.")
        else:
            print("Patient not found.")

    def delete_patient(self, patient_id):
        patient = self.search_patient(patient_id)

        if patient:
            self.patients.remove(patient)
            print("Patient record deleted successfully.")
        else:
            print("Patient not found.")