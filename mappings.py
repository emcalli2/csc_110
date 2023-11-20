def all_mappings(dictionary):
    new_tuple = []
    for key, value in dictionary.items():
        for value in dictionary[key]:
            new_tuple.append((key,value))
    return new_tuple
