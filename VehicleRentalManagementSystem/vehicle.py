from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, rent_per_day):
        self._vehicle_id = vehicle_id
        self._brand = brand
        self._model = model
        self._rent_per_day = rent_per_day

    @abstractmethod
    def display(self):
        pass