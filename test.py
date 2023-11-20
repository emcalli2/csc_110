def has_duplicate(new_list):
    new_set = list(set(new_list))
    print(new_set)
    if new_set != new_list:
        return True
    return False
print( has_duplicate([]) ) # False
print( has_duplicate([1, 2, 3, 1]) ) # True
print( has_duplicate([1, "a", "b", 4, 5]) ) # False
print( has_duplicate([1, "a", "a", 2, 3, 4]) ) # True