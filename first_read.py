#Rachel
def read_first_line(info):
    info = open('info.txt', 'r')
    line = info.readline()
    info.close()
    return line
