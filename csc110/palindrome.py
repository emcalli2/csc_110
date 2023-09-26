def reverse_string(string):
  char = ""
  index = len(string) - 1
  while index >= 0:
    char = char + string[index]
    index -= 1
  return char

def remove_spaces(string):
  index = 0
  new_string = ""
  while index < len(string):
    char = string[index]
    if char not in " ":
      new_string += char
    index += 1
  return new_string

def is_palindrome(string):
  string_2 = remove_spaces(string)
  if string_2 == reverse_string(string_2):
    return True
  else:
    return False

def main():
  print( reverse_string("aeiou") ) # uoiea
  print( remove_spaces("ae io ua") ) # aeioua
  
  print( is_palindrome("noon") ) # True
  print( is_palindrome("deified") ) # True
  print( is_palindrome("go deliver a dare vile dog") ) # True
  
main()