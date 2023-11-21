from plate_decorator import PlateDecorator


class Stuffing(PlateDecorator):
    def description(self):
        return self._plate.description() + ", Stuffing"

    def area(self):
        return self._plate.area() - 18

    def weight(self):
        return self._plate.weight() - 7

    def count(self):
        return self._plate.count() + 1
