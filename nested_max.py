# Rachel
def nested_max(lists):
    highest = None
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if highest == None or lists[i][j] > highest:
                highest = lists[i][j]
    return highest
print(nested_max([[3,3],[3,8]]))
