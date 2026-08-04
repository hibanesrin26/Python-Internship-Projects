from person import Person


class Patient(Person):

    def __init__(self, patient_id, name, age, disease):
        super().__init__(patient_id, name, age)
        self.__disease = disease

    def get_patient_id(self):
        return self._person_id

    def get_disease(self):
        return self.__disease

    def set_disease(self, disease):
        self.__disease = disease

    def display(self):
        print(f"Patient ID: {self._person_id}")
        print(f"Patient Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Disease: {self.__disease}")