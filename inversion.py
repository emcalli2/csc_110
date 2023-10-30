def invert_dictionary(dictionary):
    invert = {}
    for key, value in dictionary.items():
        if value in invert:
            invert[value].append(key)
        else:
            invert[value] = [key]
    return invert
