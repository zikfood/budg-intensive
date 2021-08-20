from django.utils.deprecation import MiddlewareMixin


class FakeUser:

    # определите у пользователя аттрибуты auth
    pass


# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):

        return self.get_response(request)

    def process_response(self, request, response):

        return response
