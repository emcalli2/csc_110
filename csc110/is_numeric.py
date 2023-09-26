#this is better than isnumeric!
def is_numeric_one_char(string):
    if len(string) !=1:
        return False
    if string in "0123456789":
        return True
    else:
        return False
def main():
    print(is_numeric_one_char("2"))
main()

