from django.db.models import Q, Count

from day_7.queryset_methods.models import Order, Customer


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """

    result = Order.objects.filter(customer__name__exact=name).count()

    return result
