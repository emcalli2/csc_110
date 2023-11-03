def count_words(file_name):
    counts = {}
    f = open(file_name, "r")
    for line in f:
        words = line.strip().split(" ")
        for w in words:
            w = w.lower()
            if w not in counts:
                counts[w] = 1
            else: 
                counts[w] += 1
    return counts
    print(count_words(info.txt))
        