from abc import ABC, abstractmethod

from ..utils.validators import validate_price


class Vehicle(ABC):
    
    def __init__(self, make: str, model: str, year: int, price: float) -> None:
        self._make = make
        self._model = model
        self._year = year
        self._price = validate_price(price)
        self._is_running = False

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        self._price = validate_price(new_price)

    @property
    def is_running(self) -> bool:
        return self._is_running

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def display_info(self) -> None:
        pass

    def stop(self) -> None:
        self._is_running = False
        print(f"{self._make} {self._model} stopped.")

    def __str__(self) -> str:
        return f"{self._year} {self._make} {self._model}"
