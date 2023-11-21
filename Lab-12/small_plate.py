from plate import Plate


class SmallPlate(Plate):
    def __init__(self):
        self._items = []

    def description(self):
        return "Small Plate"

    def area(self):
        return 78

    def weight(self):
        return 32

    def count(self):
        return len(self._items)
