'''
Elizabeth McAllister
CSC110
Project -3
This program has four functions that calculate various stat values.
'''
# this function calculates the mean 
def mean(numbers):
    '''
    This functions returns the mean of the list named numbers
    Args:
        numbers: this is a list of numbers 
    Returns: 
        The mean of the list rounded to two decimals 
    '''
    index = 0
    sum = 0
    if len(numbers) == 0:
        return 0
    # sums every element in numbers
    while index < len(numbers):
        sum += numbers[index]
        index += 1
    mean = sum / len(numbers)
    return round(mean,2)


# this function calculates the variance 
def variance(numbers):
    '''
    This functions returns the variance of the list named numbers
    Args:
        numbers: this is a list of numbers 
    Returns: 
        The variance of the list rounded to two decimals 
    '''
    mean_2 = mean(numbers)
    index = 0
    total = 0
    # sums the squares of the difference between values in numbers and mean
    while index < len(numbers):
        total += ((numbers[index] - mean_2) ** 2)
        index += 1
    variance = total / (len(numbers)-1)
    return round (variance,2)


# this function calculates the standard deviation
def sd(numbers):
    '''
    This functions returns the standard deviation of the list
    Args:
        numbers: this is a list of numbers 
    Returns: 
        The standard deviation of the list rounded to two decimals 
    '''
    standard_dev = (variance(numbers)) ** (1/2)
    return round(standard_dev,2)


# this function calculates the range of the list
def list_range(numbers):
    '''
    This functions returns the range of the list named numbers
    Args:
        numbers: this is a list of numbers 
    Returns: 
        The range (highest - lowest values) of the list 
    '''
    index = 0 
    highest = 0
    if len(numbers) == 0:
        return 0
    length = len(numbers) -1
    lowest = numbers[length]
    # itterates through numbers to find highest and lowest values 
    while index < len(numbers):
        if numbers[index] > highest:
            highest = numbers[index]
        if numbers[index] < lowest:
            lowest = numbers[index]
        index += 1
        # returns the range (highest - lowest)
    return highest - lowest
