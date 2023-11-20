def has_duplicate(list):
    new_set = set()
    for x in list:
        if x in new_set:
            return True
        new_set.add(x)
    return False
