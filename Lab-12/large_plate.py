from plate import Plate


class LargePlate(Plate):
    def __init__(self):
        self._items = []

    def description(self):
        return "Large Plate"

    def area(self):
        return 113

    def weight(self):
        return 24

    def count(self):
        return len(self._items)
