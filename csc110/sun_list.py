def sum_all(numbers):
    sum = 0 
    index = 0
    while index < len(numbers):
        sum += numbers[index]
        index += 1
    return sum
print(sum_all([1,2,1,1]))
