# Атрибуты экземпляра класса
class Car:
    model = 'BMW'
    engine = 3.6


a = Car()
b = Car()
print(Car.__dict__, '\n',
        a.__dict__, '\n',
        b.__dict__)

a.door = 4
print(Car.__dict__, '\n',
        a.__dict__, '\n',
        b.__dict__)

b.model = 'Kia'
print(Car.__dict__, '\n',
        a.__dict__, '\n',
        b.__dict__)

# a.mo =2
# Car.mo = 3
# del Car.mo
# Car.mo = 3
# del a.mo
