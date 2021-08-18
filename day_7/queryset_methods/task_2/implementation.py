from django.db.models import Q, Count, Max

from day_7.queryset_methods.models import Order, Customer


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период

    """

    result = Order.objects.values_list('customer__name')\
        .filter(date_formation__range=(begin, end))\
        .annotate(num_of_orders=Count('customer'))\
        .order_by('-num_of_orders')

    if result.exists():
        return result[0]
    else:
        return None