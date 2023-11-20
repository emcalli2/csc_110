def csv_to_list(file_name):
    f = open(file_name, 'r')
    list = []
    for line in f:
        line = line.strip("\n").split(",")
        for i in range(1,len(line)):
            if line[i].isnumeric():
                list.append(line[i])
            elif "." in line[i]:
                list.append(line[i]) 
    return list

def count_start_digits(numbers):
    dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    i = 0
    while i < len(numbers):
        first_digit = int(numbers[i][0])
        dict[first_digit] += 1
        i += 1
    return dict
print(csv_to_list("places.csv"))
list_of_numbers = csv_to_list("places.csv")
counts = count_start_digits(list_of_numbers)
print(counts) # {1: 6, 2: 3, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}