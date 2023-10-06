def concatenate(words):
    string = ""
    index = 0
    while index < len(words):
        if index == len(words) -1:
            string += words[index]
        if len(words) -1 > index:
          string += words[index] + " " 
        index += 1
    return string
