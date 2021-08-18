from django.db.models import Avg, F, IntegerField

from day_7.queryset_methods.models import OrderItem


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    result = OrderItem.objects\
        .filter(order__date_formation__range=(begin, end)) \
        .exclude(product__name__exact=product) \
        .aggregate(avg_order_cost=Avg(F('product__productcost__value') * F('count'), output_field=IntegerField()))['avg_order_cost']

    return result
