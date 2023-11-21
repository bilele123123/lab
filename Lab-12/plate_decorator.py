from plate import Plate
from abc import ABC

class PlateDecorator(ABC):
    def __init__(self, p):
        super().__init__()
        self._plate = p

    def description(self):
        return self._plate.description()

    def area(self):
        return self._plate.area()

    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()
