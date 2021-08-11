import unittest

from day_4.lambda_function.task_4.implementation import (
    a,
    res_list_product,
)


class MyTestCase(unittest.TestCase):
    def test_on_filter(self):
        self.assertEqual(res_list_product, [a])


if __name__ == '__main__':
    unittest.main()
