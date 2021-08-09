from datetime import date, timedelta, datetime


def get_next_date(some_date):

    #return some_date + timedelta(1)
    long_months = (1, 3, 5, 7, 8, 10, 12)
    short_months = (4, 6, 9, 11)
    day = some_date.day
    month = some_date.month
    year = some_date.year
    february = 2

    if day == 31:
        if month == 12:
            result = date(year + 1, 1, 1)
        elif month in long_months:
            result = date(year, month + 1, 1)

    elif day == 30 and month in short_months:
        result = date(year, month + 1, 1)

    elif month == february:
        if day == 29:
            result = date(year, 3, 1)
        elif day == 28 and (year % 4 == 0 and year % 100 != 0):
            result = date(year, february, 29)

    else:
        result = date(year, month, day + 1)

    return result

