#Rachael
def every_two_together(characters):
    string = ""
    for index in range(0, len(characters), 2):
        string += characters[index]
    return string
