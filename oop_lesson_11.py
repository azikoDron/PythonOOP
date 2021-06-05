# Практика с property
from string import digits


class User:
    def __init__(self, login, password):
        self.__login = login
        self.password = password            # сразу вызывается setter
        self.__secret = '123456'

#    @property
#    def secret(self):
#        s = input('Type your password: ')
#        if s == self.password:
#            return self.__secret
#        raise ValueError('Permission denied!')

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(password):
        for i in digits:
            if i in password:
                return True
        return False

    @password.setter
    def password(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Value must be str")
        if len(new_val) < 4:
            raise ValueError('Length must be more than 4')
        if len(new_val) >= 13:
            raise ValueError('Length must be less than 12 or equal')
        if not User.is_include_number(new_val):
            raise ValueError('Value must consists at least one digit')
        self.__password = new_val


a = User('aaa', 'aaa12')
print(a.password)
# a.secret

