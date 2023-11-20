#Rachel
def count_names(file_name):
    f = open(file_name, 'r')
    names = set()
    for line in f:
        names.add(line.strip())
    f.close()
    return len(names)