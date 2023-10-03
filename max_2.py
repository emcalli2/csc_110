def max_of_three(numbers):
    result_max = numbers[0]
    index = 0
    if len(numbers) > 0:
        while index < len(numbers):
            if numbers[index] > result_max:
               result_max = numbers[index]
        index += 1
    else: 
        return 0
    return result_max
def main():
    print(max_of_three([ ]))
main()

#This is in the midterm

