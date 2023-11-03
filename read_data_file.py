def read_csv(file_name):
    info = open(file_name,"r")
    items = {}
    line = []
    for line in info:
        line = line.strip("\n").split(",")
        key = line[0]
        values = []
        for i in range(1,len(line)):
            if line[i].isnumeric():
                values.append(int(line[i]))
            elif "." in line[i]:
                values.append(float(line[i]))
            else:
                values.append(line[i])
        items[key] = values
    info.close()
    return items

