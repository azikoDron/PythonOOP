# Property. getter и setter методы && Декоратор Property

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    # getter - метод
    def get_balance(self):
        return self.__balance

    # setter - методы
    def set_balance(self, new_balance):
        if isinstance(new_balance, (int, float)):
            self.__balance = new_balance
        else:
            raise ValueError(f'{new_balance} is not Int or Float object! ')

    def del_balance(self):
        del self.__balance

    # Property
    # Чтобы была возможность обращаться как:
    #   account_1.balance
    #   account_1.balance = 100
    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)


account_1 = BankAccount('Jimmy', 1000)
print(account_1.balance)

account_1.balance = 500
print(account_1.balance)

# del account_1.balance
# print(account_1.balance)

#################################################################################


#  Декоратор Property
class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, new_balance):
        if isinstance(new_balance, (int, float)):
            self.__balance = new_balance
        else:
            raise ValueError(f'{new_balance} is not Int or Float object! ')

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

    # balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)

    # balance = property()
    # balance = balance.setter(get_balance)
    # balance = balance.setter(set_balance)
    # balance = balance.deleter(del_balance)

account_2 = BankAccount('John', 4000)

print(account_2.my_balance)
account_2.my_balance = 100
print(account_2.my_balance)
# del account_2.my_balance
print(account_2.my_balance)
