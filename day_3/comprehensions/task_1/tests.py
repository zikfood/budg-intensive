import unittest

from day_3.comprehensions.task_1.implementation import (
    great_comprehension,
)


class MyTestCase(unittest.TestCase):
    def test_get_element_by_index(self):
        list1 = [12, 2, 17, 44, 131]
        list2 = [127, 69, 144, 0, 1024]
        list3 = [8, 6, 5, 4, 7]
        self.assertEqual(great_comprehension(list1, list2, list3), [480, 384, 672, 120, 96, 168])

if __name__ == '__main__':
    unittest.main()