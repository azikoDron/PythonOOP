# Магические методы __str__, __repr__, __len__, __abs__. dander method(double underscore)

class Robot:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The Robot object {self.name}'

    def __str__(self):
        return 'Robot object'


print(Robot)

a = Robot('Bender')


print(a)

#                                   __len__, __abs__
