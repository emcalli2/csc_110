def tally_negatives(numbers):
    result = {}
    for n in numbers:
        if n < 0:
            if n not in result:
                result[n] = 0
            result[n] += 1
    return result

print(tally_negatives([1,-2]))