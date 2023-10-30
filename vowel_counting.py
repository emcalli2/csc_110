def count_vowels(string):
    counts = {"a":0, "e":0, "i":0, "o":0, "u":0, "A":0, "E":0, "I":0, "O":0, "U":0}
    for index in range(len(string)):
        if string[index] in counts:
            counts[string[index]] += 1
    return counts
print( count_vowels("") ) # {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0,
                          #  "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
                
print( count_vowels("banana") ) # {"a": 3, "e": 0, "i": 0, "o": 0, "u": 0,
                                #  "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
                                
print( count_vowels("Adriana") ) # {"a": 2, "e": 0, "i": 1, "o": 0, "u": 0,
                                 #  "A": 1, "E": 0, "I": 0, "O": 0, "U": 0}
                                 
print( count_vowels("Hello World!") ) # {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0,
                                      #  "A": 0, "E": 0, "I": 0, "O": 0, "U": 0}