class Coffee:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def cappuccino(cls):
        return cls(('espresso', 'milk'))

    @classmethod
    def latte(cls):
        return cls(('espresso', 'milk', 'milk foam'))

    @classmethod
    def glace(cls):
        return cls(('espresso', 'milk', 'icecream'))
