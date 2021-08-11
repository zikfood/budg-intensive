class Tuple:
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def __init__(self, *args):
        self.values = args

    def __getitem__(self, item):
        return self.values[item]

    def __str__(self):
        return str(self.values)

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
        if value not in self.values:
            raise ValueError

        for count, item in enumerate(self.values):
            if item == value:
                return count
