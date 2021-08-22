import time

from django.utils.deprecation import MiddlewareMixin


class FakeUser:

    def __init__(self, auth=False):
        self.auth = auth


class MyMiddleware(MiddlewareMixin):

    VALID_TOKEN = 'VALID_TOKEN'
    INVALID_TOKEN = 'INVALID_TOKEN'
    request_start_time = 0

    def process_request(self, request):
        if request.auth == self.VALID_TOKEN:
            request.auth = True
        elif request.auth == self.INVALID_TOKEN:
            request.auth = False

        self.request_start_time = time.time()
        time.sleep(1)

        return self.get_response(request)

    def process_response(self, request, response):
        request_runtime = time.time() - self.request_start_time
        request.runtime = request_runtime
        return response


'''
AuthenticationMiddleware - Связывает пользователей, использующих сессии, запросами.
SessionMiddleware - Управление сессиями между запросами. Позволяет сохранять и получать данные посетителя сайта
CsrfViewMiddleware - включает CSRF защиту. Предотвращает подделку запроса с помощью проверки наличия CSRF токена
'''