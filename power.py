def power(base,exp):
    number = 1
    n = 1
    while n <= exp:
        number *= base
        n += 1
    return number
print(power(2,3)) 