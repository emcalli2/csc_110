print("ADD COMMENTS, DO NOT SUBMIT")
def mean(numbers):
    index = 0
    sum = 0
    if len(numbers) == 0:
        return 0
    while index < len(numbers):
        sum += numbers[index]
        index += 1
    mean = sum / len(numbers)
    return round(mean,2)



def variance(numbers):
    mean_2 = mean(numbers)
    index = 0
    result = 0
    while index < len(numbers):
        result += ((numbers[index] - mean_2) ** 2)
        index += 1
    var = result / (len(numbers)-1)
    return round (var,2)


def sd(numbers):
    standard_dev = (variance(numbers)) ** (1/2)
    return round(standard_dev,2)

def list_range(numbers):
    index = 0 
    highest = 0
    if len(numbers) == 0:
        return 0
    length = len(numbers) -1
    lowest = numbers[length]
    while index < len(numbers):
        if numbers[index] > highest:
            highest = numbers[index]
        if numbers[index] < lowest:
            lowest = numbers[index]
        index += 1
    return highest - lowest


def main():
  value = mean([])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}" 
  
  value = mean([0, 0, 0])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}" 
  
  value = mean([4, 5, 2])
  assert value == 3.67, \
      f"expected return value was 3.67, but function returned {value}" 
  
  value = variance([4, 5, 2])
  assert value == 2.33, \
      f"expected return value was 2.33, but function returned {value}" 
  
  value = sd([4, 5, 2])
  assert value == 1.53, \
      f"expected return value was 1.53, but function returned {value}"
  
  value = list_range([4, 5, 2])
  assert value == 3, \
      f"expected return value was 3, but function returned {value}"
  
  value = list_range([])
  assert value == 0, \
      f"expected return value was 0, but function returned {value}"

  print("All tests passed.")

main()

