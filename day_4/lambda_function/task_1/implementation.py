from operator import itemgetter

my_list = [(2, 2), (6, 13), (55, 3), (4, 8)]

# вместо лямбды можно itemgetter(1)

res_list = sorted(my_list, reverse=True, key=lambda value: value[1])