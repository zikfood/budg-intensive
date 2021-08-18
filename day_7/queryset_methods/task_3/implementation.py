from django.db.models import F

from day_7.queryset_methods.models import Order, ProductCost, OrderItem


def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    result = Order.objects.values_list('number')\
        .filter(date_formation__range=(begin, end))\
        .annotate(order_cost=F('orderitem__product__productcost__value') * F('orderitem__count'))\
        .order_by('-order_cost')

    if result.exists():
        return result[0]
    else:
        return None