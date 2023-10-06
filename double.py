def double(list):
    index = 0
    while index < len(list):
        list[index] *= 2
        index += 1
    return list
print(double([1,2]))