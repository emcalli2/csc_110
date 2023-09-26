def absolute(n):
    if n < 0:
        return -1 * n
    else:
        return n  

def main():
    print(absolute(-4))
    print(absolute(4))
    print(absolute(0))
main()