def frequency():
    file = input("Enter file name: ")
    fhand = open(file)
    words = fhand.read().split()
    Freq = {}
    for word in words:
        Freq[word] = Freq.get(word, 0) +1
    print(Freq)


frequency()
