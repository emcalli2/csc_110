# Rachel
def four_letter_anagram(string,a,b,c,d):
    a = string[a]
    b = string[b]
    c = string[c]
    d = string[d]
    return a + b + c + d
def main():
    print(four_letter_anagram("balm", 2, 1, 3, 0))
    print(four_letter_anagram("loin", 0, 2, 1, 3))
    print(four_letter_anagram("lugs", 3, 0, 1, 2))
    print(four_letter_anagram("reap", 3, 1, 2, 0))
main()