# Моносостояния для всех экземпляров

class Car:
    __shared_attr = {
        'model': 'BMW',
        'door': 4
    }

    def __init__(self):
        self.__dict__ = Car.__shared_attr


a = Car()
b = Car()

a.model = 'Kia'

print(a.model, b.model)
