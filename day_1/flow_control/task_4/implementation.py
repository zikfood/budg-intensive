from datetime import date, timedelta, datetime


def get_next_date(some_date):

    #return some_date + timedelta(1)
    long_months = (1, 3, 5, 7, 8, 10, 12)
    short_months = (4, 6, 9, 11)

    if some_date.day == 31:
        if some_date.month == 12:
            result = date(some_date.year + 1, 1, 1)
        elif some_date.month in long_months:
            result = date(some_date.year, some_date.month + 1, 1)

    elif some_date.day == 30 and some_date.month in short_months:
        result = date(some_date.year, some_date.month + 1, 1)

    elif some_date.month == 2:
        if some_date.day == 29:
            result = date(some_date.year, 3, 1)
        elif some_date.day == 28 and (some_date.year % 4 == 0 and some_date.year % 100 != 0):
            result = date(some_date.year, 2, 29)

    else:
        result = date(some_date.year, some_date.month, some_date.day + 1)

    return result

