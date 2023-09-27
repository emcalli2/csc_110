def sum_all(numbers):
    index = 0
    sum = 0
    while index < len(numbers):
        sum = sum + numbers[index]
        index += 1
def main():
  value = sum_all([])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([0, 0, 0, 0, 0])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([1, -1, 2, -2, 3, -3])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([1, 2, 3, 4, 5])
  assert value == 15, f"expected return value was 15, but function returned {value}" 

  print("All tests passed.")

main()