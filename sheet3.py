def grade():
    Grade = eval(input("Enter your score: "))
    if 90 <= Grade <= 100 :
        letter = 'A'
    elif 80 <= Grade:
        letter = 'B'
    elif 70 <= Grade:
        letter = 'C'
    elif 60 <= Grade:
        letter = 'D'
    elif 0 <= Grade:
        letter = 'F'
    else:
        return 'Enter valid score(-_-)'
    return letter

# print(grade())


def classifier():
    Credits = eval(input("How many credit hours you earned? "))
    if Credits >= 26:
        student = 'Senior'
    elif Credits >= 16:
        student = 'junior'
    elif Credits >= 7:
        student = 'sophomore'
    elif Credits >= 0:
        student = 'Freshman'
    else:
        return 'Enter a valid number(-_-)'
    return student

# print(classifier())


def easter():
    year = int(input("Enter a year between 1982-2048: "))
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a+24)%30
        e = (2*b+4*c+6*d+5)%7
        date = 22 + d + e
        if date > 31:
            Easter = 'April {}'.format(date-31)
        else:
            Easter = 'March {}'.format(date)
    else:
        return 'Enter year betwen 1982-2048 only(-_-)'
    return Easter


# print(easter())


def leap(year):
    #year = int(input('Enter a year: '))
    if year %4 == 0:
        if year %100 ==0 :
            if year %400 == 0:
                Year = 'It\'s a leep year'
            else:
                Year = 'It\'s not a leep year'
        else:
            Year = 'It\'s a leep year'
    else:
        Year = 'It\'s not a leep year'
    return Year


# print(leap(2020))


def valid_date():
    flag = False
    date = input("Enter date: day/month/year: ")
    date_list = date.split('/')
    day, month, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
    if year > 0 and 1 <= month <= 12:
        if month == ((1),(3),(5),(7),(8),(10),(12)):
            if 1 <= day <=31:
                flag = True
        elif month == 2:
            if leap(year) == 'It\'s a leep year':
                if 1 <= day <=29:
                    flag = True
            else:
                if 1 <= day <=28:
                    flag = True
        else:
            if 1 <= day <=30:
                flag = True
    return flag


# print('date is valid?', valid_date())


def median():
    list = []
    a, b, c = eval(input("Enter a, b, c: "))
    list.append(a)
    list.append(b)
    list.append(c)
    list.sort()
    return 'median is {}'.format(list[1])


print(median())




