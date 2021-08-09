def convert_temperature(value, to_scale):
    if to_scale == "F":
        result = value * 9 / 5 + 32
    elif to_scale == "C":
        result = (value - 32) * 5 / 9
    else:
        result = value

    return result
