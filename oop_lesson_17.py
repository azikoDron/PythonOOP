# Наследования делегирование (Delegating)
class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def move(self):
        return "Person moves"

    def swim(self):
        return "Person swim"


class Robot(Person):

    def __init__(self, name, surname, age, material):
        super().__init__(name, surname, age)
        self.material = material

    def move(self):
        return f"Robot {self.name} move"

    def swim(self):
        return f"Robot {self.name} can not swim :("


a = Robot("Bender", 20, 20, "Steal")

b = Person("Billy", "Ivanov", 35)
