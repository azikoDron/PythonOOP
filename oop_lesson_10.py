# Вычисляем Property
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_val):
        self.__side = new_val
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side**2
        return self.__area


a = Square(4)

print(a.area())