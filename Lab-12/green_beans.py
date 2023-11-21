from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):
    def description(self):
        return self._plate.description() + ", Green Beans"

    def area(self):
        return self._plate.area() - 20

    def weight(self):
        return self._plate.weight() - 3

    def count(self):
        return self._plate.count() + 1