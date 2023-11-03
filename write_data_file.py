def write_csv(dictionary, file_name):
    info = open(file_name, "w")
    line = ""
    for key, value in dictionary.items():
        line += key 
        for item in value:
            line += "," + str(item)
        line += "\n"  
    info.write(line)
    info.close()
