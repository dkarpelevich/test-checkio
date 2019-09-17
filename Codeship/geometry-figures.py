import math as m

class Parameters:
    figure = None

    def __init__(self, param):
        self.param = param

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        return self.figure.perimeter(self.param)

    def area(self):
        return self.figure.area(self.param)

    def volume(self):
        return self.figure.volume(self.param)

class Figure:
    def perimeter(self, param):
        raise NotImplementedError

    def area(self, param):
        raise NotImplementedError

    def volume(self, param):
        raise NotImplementedError

class Circle(Figure):
    def perimeter(self, radius):
        return round(2*m.pi*radius, 2)

    def area(self, radius):
        a = round(m.pi * radius**2, 2)
        return a

    def volume(self, radius):
        return 0

class Triangle(Figure):
    def perimeter(self, param):
        return round(param*3, 2)

    def area(self, param):
        return round(m.sqrt(3)*param**2/4, 2)

    def volume(self, param):
        return 0

class Square(Figure):
    def perimeter(self, param):
        return round(param*4, 2)

    def area(self, param):
        return round(param**2, 2)

    def volume(self, param):
        return 0

class Pentagon(Figure):
    def perimeter(self, param):
        return round(param*5, 2)

    def area(self, param):
        return round((5*param**2) / (4*m.tan(m.pi/5)), 2)

    def volume(self, param):
        return 0

class Hexagon(Figure):
    def perimeter(self, param):
        return round(param*6, 2)

    def area(self, param):
        return round((6 * param ** 2) / (4 * m.tan(m.pi/6)), 2)

    def volume(self, param):
        return 0

class Cube(Figure):
    def perimeter(self, param):
        return round(param*12, 2)

    def area(self, param):
        return round(6 * param**2, 2)

    def volume(self, param):
        return round(param**3, 2)

if __name__ == '__main__':
    figure = Parameters(10)
    figure.choose_figure(Hexagon())
    assert figure.area() == 259.81
