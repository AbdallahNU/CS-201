def acronym():
    phrase = input("Enter your phrase: ")
    List = phrase.split()
    acr = ''
    for word in List:
        letter = word[0].capitalize()
        acr += letter
    return acr


# print(acronym())


def name_value():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    name = input("Enter a name: ").lower()
    value = 0
    for letter in name:
        value += (letters.index(letter)+1)
    return value


print(name_value())


def word_count():
    sentence = input("Enter a sentence: ")
    List = sentence.split()
    return len(List)


# print(word_count())


def average_word_len():
    sentence = input("Enter a sentence: ")
    List = sentence.split()
    letters = 0
    for word in List:
        letters += len(word)
    return letters/len(List)


# print(average_word_len())
