# Публичные, приватные защищенные атрибуты и методы

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # Public
    # def show_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # # protected
    # def show_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    # Private ИНКАПСУЛЯЦИЯ - делается метод для пользователь, для работы с данными
    def show_private_data(self):
        print(self.__name, self.__balance, self.__passport)
    # можно Инкапсулировать Методы
        # def show_public_data(self):
        #     self.__show_private_data()
        # def __show_private_data(self):
        #     print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Jimmy', 1000, 468433)


# public
# print(account1.name,
#       account1.balance,
#       account1.passport)

# protected
# print(account1._name,
#       account1._balance,
#       account1._passport)

# Private
account1.show_private_data()    #ИНКАПСУЛЯЦИЯ - делается метод для пользователь, для работы с данными
# NOT CALLABLE FROM OUT OF OBJECT !!!
# print(account1.__name,
#       account1.__balance,
#       account1.__passport)

# Но полностью закрыть доступ нельзя
print(account1.__dict__)
print(account1._BankAccount__name)