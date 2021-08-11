import math
from math import sqrt


def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """

    result = [(a % 10 * 2) * int(sqrt(b)) * c for a in list1 for b in list2 for c in list3
              if a % 10 == int(str(a)[0]) and a // 10 != 0
              and b % 2 == 0 and len(str(b)) == 3
              and (c % 2 != 0 or c == 4)]
    return result
