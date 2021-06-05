# Пространство имен класса
MAX_ID = 5

class IdSetter:
    MAX_ID = 1

    def info(self):
        print(MAX_ID)
        print(self.MAX_ID)

    def info_2(self):
        print(IdSetter.MAX_ID)

    def adding_id(self):
        IdSetter.MAX_ID = IdSetter.MAX_ID + 1

    @staticmethod
    def info_3():
        print(MAX_ID, IdSetter.MAX_ID)

    @classmethod
    def info_4(cls):
        print(cls.MAX_ID, IdSetter.MAX_ID)


a = IdSetter()
print(a.info())
print(a.info_2())
print(a.info_3())
print(a.info_4())
print('#'*30)
a.adding_id()
print(IdSetter.MAX_ID, a.MAX_ID)
print(a.info())