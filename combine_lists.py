def combine(list_1,list_2):
    index = 0 
    list = ""
    while index < len(list_2):
        list = list_1.append(list_2[index])
        index += 1
    return list

