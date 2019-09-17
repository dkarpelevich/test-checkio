import math as m

class Parameters:
    figure = None

    def __init__(self, param):
        self.param = param

    def choose_figure(self, figures):
        self.figure = figures

    def perimeter(self):
        return round(self.figure.perimeter(self.param), 2)

    def area(self):
        return round(self.figure.area(self.param), 2)

    def volume(self):
        return round(self.figure.volume(self.param), 2)

class Circle:
    def perimeter(self, radius):
        return 2*m.pi*radius

    @staticmethod
    def area(radius):
        a = m.pi * radius**2
        return a

    @staticmethod
    def volume(radius):
        return 0

class Triangle:
    def perimeter(self, param):
        return param*3

    def area(self, param):
        return m.sqrt(3)*param**2/4

    def volume(self, param):
        return 0

class Square:
    def perimeter(self, param):
        return param*4

    def area(self, param):
        return param**2

    def volume(self, param):
        return 0

class Pentagon:
    def perimeter(self, param):
        return param*5

    def area(self, param):
        return (5*param**2) / (4*m.tan(m.pi/5))

    def volume(self, param):
        return 0

class Hexagon:
    def perimeter(self, param):
        return param*6

    def area(self, param):
        return (6 * param ** 2) / (4 * m.tan(m.pi/6))

    def volume(self, param):
        return 0

class Cube:
    def perimeter(self, param):
        return param*12

    def area(self, param):
        return 6 * param**2

    def volume(self, param):
        return param**3

if __name__ == '__main__':
    figure = Parameters(10)
    figure.choose_figure(Hexagon())
    assert figure.volume() == 0
