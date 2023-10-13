def flatten(numbers):
    list = []
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            list.append(numbers[i][j])
    return list