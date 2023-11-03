#Rachel
def read_first_line(filename):
    info = open(filename, 'r')
    line = info.readline()
    info.close()
    return line
