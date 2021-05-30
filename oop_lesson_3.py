# Функция как атрибуты класса
class Car:
    model = 'BMW'
    engine = 3.6

    @staticmethod
    def drive():     # self не указываем
        print("Let's go")


a = Car()
print('Функция :', Car.drive, '\n',
      'Метод :', a.drive)

Car.drive()
# a.drive()
# TypeError: drive() takes 0 positional arguments but 1 was given
#   To fix:
#       @staticmethod
#       def drive():
#           ...



