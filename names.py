# Rachel
def count_names(file_name):
    f = open(file_name, 'r')
    count = 0
    new_dict = {}
    for line in f:
        list = line.strip()
        if list not in new_dict and list != "":
    f.close()
    return len(new_dict)
    