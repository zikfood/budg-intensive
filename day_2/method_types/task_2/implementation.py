from day_2.common import MyException


class ClassFather:
    _name = ""
    registered_list = set()

    @classmethod
    def register(cls):
        if cls == ClassFather:
            raise MyException
        ClassFather.registered_list.add(cls._name)

    @classmethod
    def get_name(cls):
        if cls == ClassFather:
            raise MyException
        elif cls._name not in ClassFather.registered_list:
            raise MyException
        return cls._name


class User1(ClassFather):
    _name = 'User1'


class User2(ClassFather):
    _name = 'User2'

