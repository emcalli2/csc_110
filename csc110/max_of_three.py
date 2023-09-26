def max3(x,y,z):
    if x >= y and x >= z:
        return x
    elif y >= z and y >= x:
        return y
    elif z >= y and z >= x:
        return z
    else:
        return x
print(max3(1,1,1))
