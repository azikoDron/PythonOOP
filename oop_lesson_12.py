# classmethod and staticmethod


class Task:
    def __init__(self, task_id, task_name, task_text=''):
        self.__task_id = task_id
        self.__task_name = task_name
        self.__task_text = task_text

    @property
    def name(self):
        return self.__task_name

    @name.setter
    def name(self, new_name):
        self.__task_name = new_name

    @staticmethod
    def task_timer():
        print("static method print")

    @classmethod
    def name_cheker(cls):
        cls.name = 'fff'
        print('classmethod print, ', cls)

a= Task('1', 'one')