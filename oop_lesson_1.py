# Class attributes # Атрибуты класса
class Car:
    model = 'BMW'
    engine = 3.6


a = Car()

print(a.model)

b = Car()
a.model = 'Audi'
print(a.model, b.model)

# getattr()
# setattr()
# delattr()
# У кого уже менялся атрибут, тот неуязвимый (область видимости)
Car.model = 'Kia'
print(a.model, b.model)

Car.door = 4
print(a.door, b.door)

#del Car.door
print(a.door, b.door)
