def keys_and_values(dictionary):
    list = []
    for key, value in dictionary.items():
        list.append(key)
        list.append(value)
    return list
def main():
    print(keys_and_values({'A': 10, 'B': 25, 'C': 27, 'D': 10, 'E': 5}))

main()