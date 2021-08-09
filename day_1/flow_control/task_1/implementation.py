def get_numbers(min_num=1000, max_num=2000):

    numbers = []
    for num in range(min_num, max_num + 1):
        if (num % 7 == 0) and (num % 5 != 0):
            numbers.append(num)
    return numbers
