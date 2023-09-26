def sqrt(n):
    return n ** (1/2)
def hypotenuse(a,b):
    c = sqrt(a**2 + b**2)
    return round(c,2)

def main():
    print(hypotenuse(10,10))
    print(hypotenuse(3,4))
main()
