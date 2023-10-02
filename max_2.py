def max_of_three(numbers):
    result_max = numbers[0]
    index = 0
    while result_max < numbers[index]:
        result_max = numbers[index]
        index += 1
    return result_max
print(max_of_three([1,2,3]))



