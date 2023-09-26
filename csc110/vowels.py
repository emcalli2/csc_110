def count_vowels(string):
    index = 0
    count = 0
    while index < len(string): 
        if string[index] in "aeiouAEIOU":
            count = count + 1
        index += 1
    return count

def main():
  print( count_vowels("") ) # 0
  print( count_vowels("aaa") ) # 3
  print( count_vowels("AEIOU") ) # 5
  print( count_vowels("cysts") ) # 0
  
main()
        