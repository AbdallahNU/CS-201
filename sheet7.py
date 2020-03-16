def wc():
    file = input("Enter file name: ")
    fhand = open(file)
    lines = fhand.readlines()
    line_count = len(lines)
    word_count, char_count = 0, 0
    for line in lines:
        words = line.split()
        word_count += len(words)
        for word in words:
            char_count += len(word)
    print('line_count-->{0}\n word_count-->{1}\n char_count-->{2}'.format(line_count, word_count, char_count))


# wc()

def average():
    file = input("Enter file name: ")
    fhand = open(file)
    words = fhand.read().split()
    char_count = 0
    for word in words:
        char_count += len(word)
    return char_count/len(words)


# print(average())

# I made it Now it will not print anything except numbers from 0 to 10

def hist():
    file = input("Enter file name: ")
    lines = open(file).readlines()
    grades = {}
    for line in lines:
        line = line.strip()
        try:
            grade = eval(line)
        except:
            continue
        if grade in range(11):
            grades[line] = grades.get(line, 0) +1
    for i in grades:
        print(i,'-->', '*'*grades[i])

hist()
