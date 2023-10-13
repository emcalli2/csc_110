def indices_of_vowel(string):
    result = []
    for index in range(len(string)):
        if string[index] in "aeiouAEIOU":
            result.append(index)
        return result

print(indices_of_vowel("hello"))

