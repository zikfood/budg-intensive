def count_lines(filename):
    with open(filename) as file:
        num_lines = sum(1 for _ in file)
    print(num_lines)
