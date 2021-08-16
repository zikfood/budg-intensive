import django
from django.conf import settings
from django.core import management

settings.configure(
    INSTALLED_APPS=[
        'day_7.queryset_methods',
        'day_7.queryset_methods.task_1',
        'day_7.queryset_methods.task_2',
        'day_7.queryset_methods.task_3',
        'day_7.queryset_methods.task_4',
        'day_7.queryset_methods.task_5',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    },
    DEBUG=True,
)
django.setup()
management.call_command('makemigrations', 'queryset_methods')
management.call_command('migrate')
