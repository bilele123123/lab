from plate_decorator import PlateDecorator


class Potatoes(PlateDecorator):
    def description(self):
        return self._plate.description() + ", Potatoes"

    def area(self):
        return self._plate.area() - 18

    def weight(self):
        return self._plate.weight() - 6

    def count(self):
        return self._plate.count() + 1
