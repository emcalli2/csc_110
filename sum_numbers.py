#Rachel
def sum_all(file_name):
    total = 0
    info = open(file_name, "r")
    for line in info:
        numbers = int(line.strip("\n"))
        total += numbers
    return total
