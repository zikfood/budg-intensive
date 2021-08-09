def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    months = {
        "январь": 31, "февраль": 29, "март": 31, "апрель": 30, "май": 31, "июнь": 30,
        "июль": 31, "август": 31, "сентябрь": 30, "октябрь": 31, "ноябрь": 30, "декабрь": 31}

    for item in dict.keys(months):
        if item == month:
            result = months[month]
            break
    else:
        result = 0

    return result
