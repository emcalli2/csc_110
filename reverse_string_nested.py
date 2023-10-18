def reverse_string_nested(strings):
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            strings[i][j] = strings[i][j][::-1]
    return strings
print(reverse_string_nested([["desserts"], ["raw"]]))