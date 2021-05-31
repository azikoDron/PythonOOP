# Методы инициализации
class Robot:

    # skin = 'Steal'
    # def set_value(self, value, age=0):
    #     self.name = value
    #     self.age = age

    def __init__(self, name, year=2002, skin='Steal'):
        self.name = name
        self.year = year
        self.skin = skin


bender = Robot('Bender', 2000, 'Gold')