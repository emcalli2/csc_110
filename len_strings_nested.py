def len_strings_nested(strings):
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            strings[i][j] = len(strings[i][j])
    return strings
print(len_strings_nested([["dessert"],["live"]]))