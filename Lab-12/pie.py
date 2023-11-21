from plate_decorator import PlateDecorator


class Pie(PlateDecorator):
    def description(self):
        return self._plate.description() + ", Pie"

    def area(self):
        return self._plate.area() - 19

    def weight(self):
        return self._plate.weight() - 8

    def count(self):
        return self._plate.count() + 1
