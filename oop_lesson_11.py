# Практика с property
class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Value must be str")
        if len(new_val) < 4:
            raise ValueError('Length must be more than 4')
        if len(new_val) >= 13:
            raise ValueError('Length must be less than 12 or equal')
        self.__password = new_val

