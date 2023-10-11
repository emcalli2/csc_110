def shift_left(items):
    index = 0
    while index < len(items) - 1:
        items[index] = items[index+1]
        index += 1
    items[index] = None
    return items
print(shift_left([1,2,3]))

def shift_right(items):
    index = len(items) -1
    while index > 0:
        items[index] = items[index - 1]
        index -= 1
    items[index] = None
    return items
print(shift_right([1,2,3,4]))