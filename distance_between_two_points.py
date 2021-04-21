import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.distance_to_origin()

    def distance_to_origin(self):
        res = math.sqrt(self.x ** 2 + self.y ** 2)
        return res

    def reflect(self, axis):
        if axis == 'x':
            self.y = -self.y
        if axis == 'y':
            self.x = -self.x
        else:
            print('Invalid input')


pt = Point(x=float(input('Enter the point for x-axis:')), y=float(input('Enter the point for y-axis:')))
print(pt.distance_to_origin())
pt.reflect(axis=input('Enter the axis to be reflected:'))

