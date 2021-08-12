class Multiplier:
    multiplier = 1
    multiply_result = 0

    def __init__(self, value) -> None:
        super().__init__()
        self.multiply_result = value * self.multiplier

    def get_value(self) -> int:
        return self.multiply_result

    def __int__(self):
        return int(self.multiply_result)

    def __add__(self, value):
        if isinstance(value, Multiplier):
            return Multiplier(self.multiply_result + int(value))

    def __sub__(self, value):
        if isinstance(value, Multiplier):
            return Multiplier(self.multiply_result - int(value))

    def __mul__(self, value):
        if isinstance(value, Multiplier):
            return Multiplier(self.multiply_result * int(value))

    def __truediv__(self, value):
        if isinstance(value, Multiplier):
            return Multiplier(self.multiply_result / int(value))


class Hundred(Multiplier):
    """Множитель на 100"""
    multiplier = 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    multiplier = 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    multiplier = 1000000
