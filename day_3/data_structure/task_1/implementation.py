class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *args):
        self.values = args

    def __getitem__(self, item):
        return self.values[item]

    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        result = 0
        for item in self.values:
            if item == value:
                result += 1
        return result

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        if value > len(self.values):
            raise ValueError

        value_index = 0
        try:
            for item in self.values:
                if item == value:
                    return value_index
                value_index += 1
        except:
            raise ValueError
