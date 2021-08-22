from mock import Mock
from .middlewares import MyMiddleware
import unittest


class TestCase(unittest.TestCase):

    def test_init(self) -> None:
        self.middleware = MyMiddleware('response')
        self.assertEqual(self.middleware.get_response, 'response', 'Миддлвэйр объект не верно проинициализирован')

    def test_is_time(self):
        request = Mock()
        middleware = MyMiddleware(Mock())
        middleware(request)
        if isinstance(request.runtime, float):
            self.assertGreater(request.runtime, 0, f'Время исполнения запроса не может быть меньше 0')
        else:
            raise AssertionError(
                'У объекта request отсутствует аттрибут runtime'
            )

    def test_auth(self):
        request = Mock()
        request.auth = 'INVALID_TOKEN'
        middleware = MyMiddleware(Mock())
        middleware(request)

        self.assertFalse(request.auth, "Юзер не должен быть авторизован")


if __name__ == '__main__':
    unittest.main()
