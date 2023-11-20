'''
Elizabeth McAllister
CSC110
Project -4
This program has four functions that check benford's law for a file
'''
# This function opens a file in read mode to obtain a list of numbers
def csv_to_list(file_name):
    '''
    This functions returns a list of all the numbers in a file
    Args:
        file_name: a data file
    Returns: 
        a list of all of the elements of the file that are numeric
    '''
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

# this function counts the occurances of a digit
def count_start_digits(numbers):
    '''
    This functions returns a dictionary counting number of leading digit occurences
    Args:
        numbers: a list of digits from the file
    Returns: 
        a dictionary showing the number of occurances of the leading digits
    '''
    dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    i = 0
    while i < len(numbers):
        if numbers[i][0] in dict:
            first_digit = int(numbers[i][0])
            dict[first_digit] += 1
        i += 1
    return dict

# This function calculates the percentage of occurances of a digit
def digit_percentages(counts):
    '''
    This functions returns a dictionary of the percentage
    Args:
        counts: a dictionary of the number of occurances of a digit
    Returns: 
        the percentage of times that leading digit appears
    '''
    percentages = {}
    total = 0 
    # iterates through counts to sum the values
    for values in counts.values():
        total += values
    print(values)
    for digit, count in counts.items():
        percentages[digit] = round((count / total) * 100, 2)
    return percentages


def check_benfords_law(percentages):
    '''
    This functions returns whether or not the data follows benford's law
    Args: 
        percentages: the percent that each leading digit occurs
    Returns: 
        True: if the file follows benford's law
        False: if the file does not follow benford's law
    '''
    law = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    # checks if the percentage of each digit is within bounds
    for key,value in percentages.items():
        if value < (law[key] - 5) or value > (law[key] + 10):
            return False
    return True

list_of_numbers = csv_to_list("populations.csv")
counts = count_start_digits(list_of_numbers)
percentages = digit_percentages(counts)
