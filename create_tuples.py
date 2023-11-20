def zip_lists(list_1,list_2,list_3):
    new_tuple = []
    for i in range(len(list_1)):
        new_tuple.append((list_1[i] , list_2[i] , list_3[i]))
    return new_tuple
print( zip_lists([1, 2], ["a", "b"], [1.0, 2.0]) ) # [(1, "a", 1.0), (2, "b", 2.0)]
print( zip_lists([], [], []) ) # []