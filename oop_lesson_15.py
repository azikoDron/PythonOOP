# Полиморфизм

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count(self):                # ONE METHOD FOR ALL
        return self.x * self.y


class Square:
    def __init__(self, x):
        self.x = x

    def count(self):                # ONE METHOD FOR ALL
        return self.x ** 2


