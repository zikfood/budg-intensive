from day_2.common import MyException


class Value:
    class_value = 0

    def __init__(self, value):
        self.class_value = value

    def __add__(self, other):
        try:
            return self.class_value + other
        except:
            raise MyException

    def __sub__(self, other):
        try:
            return self.class_value - other
        except:
            raise MyException

    def __mul__(self, other):
        try:
            return self.class_value * other
        except:
            raise MyException

    def __truediv__(self, other):
        try:
            return self.class_value / other
        except:
            raise MyException

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        try:
            return other - self.class_value
        except:
            raise MyException

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        try:
            return other / self.class_value
        except:
            raise MyException
