from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):
    def description(self):
        return self._plate.description() + ", Turkey"

    def area(self):
        return self._plate.area() - 15

    def weight(self):
        return self._plate.weight() - 4

    def count(self):
        return self._plate.count() + 1
