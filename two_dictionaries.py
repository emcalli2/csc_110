# Rachel
def merge_dictionaries(dict_1,dict_2):
    for key, value in dict_2.items():
        if key in dict_1:
            dict_1[key] += value
        else:
            dict_1[key] = value
    return dict_1
