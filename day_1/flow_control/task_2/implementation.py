def convert_temperature(value, to_scale):
    if to_scale == "F":
        return value * 9 / 5 + 32
    if to_scale == "C":
        return (value - 32) * 5 / 9
    return value
