from vehicle import Vehicle


class Rental(Vehicle):

    def __init__(self, vehicle_id, brand, model, rent_per_day, days):
        super().__init__(
            vehicle_id,
            brand,
            model,
            rent_per_day
        )

        self.__days = days

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_days(self):
        return self.__days

    def set_days(self, days):
        self.__days = days

    def calculate_charge(self):
        return self._rent_per_day * self.__days

    def display(self):
        print(f"Vehicle ID: {self._vehicle_id}")
        print(f"Brand: {self._brand}")
        print(f"Model: {self._model}")
        print(f"Rent Per Day: {self._rent_per_day}")
        print(f"Rental Days: {self.__days}")
        print(f"Total Charge: {self.calculate_charge()}")