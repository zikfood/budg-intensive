def return_errors(filename):
    """
    Функция, которая возвращает строки из лога со словом error
    """
    error_line = "ERROR"
    with open(filename) as file:
        for line in file:
            if error_line in line:
                yield line


x = return_errors('log.txt')


