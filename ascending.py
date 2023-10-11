def stop_ascending(list):
    index = 0
    if len(list) == 0:
        return None
    for index in range(1, len(list)):
        if list[index] <= list[index -1]:
            return index
    return len(list)
