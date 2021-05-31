# Практический пример
from math import sqrt   # для нахождения квадратного корня


class Point:
    point_list = []

    def __init__(self, coordinate_x=0, coordinate_y=0):
        self.x = coordinate_x
        self.y = coordinate_y
        # self.move_to(coordinate_x, coordinate_y)  # DRY)
        Point.point_list.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Coordinates are ({self.x}, {self.y})')

    def distance_calc(self, next_point):
        if not isinstance(next_point, Point):
            raise ValueError('The argument must be the Point object')
        return sqrt((self.x - next_point.x)**2 + (self.y - next_point.y)**2)
