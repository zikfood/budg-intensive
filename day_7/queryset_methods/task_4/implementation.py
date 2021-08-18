from django.db.models import Sum, IntegerField

from day_7.queryset_methods.models import OrderItem


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    result = OrderItem.objects.values('product__name')\
        .filter(order__date_formation__range=(begin, end))\
        .annotate(amount_of_orders=Sum('count',output_field=IntegerField()))\
        .order_by('-amount_of_orders')

    if result.exists():
        return [result[0]]
    else:
        return []
