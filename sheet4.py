def fibonaccii():
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    c = a + b
    list = [a, b]
    for i in range(n):
        list.append(c)
        a = b
        b = c
        c = a + b
    return('fibonacci sequence: {0}\nnth fibonaccii number: {1}'.format(list, list[n-1]))


# print(fibonaccii())


def investment():
    initial = 1
    double = 2*initial
    years = 1
    interest_rate = eval(input("Enter annual interest rate: "))
    while initial < double:
        years +=1
        initial = initial + initial*interest_rate
    return years


# print(investment())


def prime():
    n = int(input("Enter a number: "))
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return '{0} is prime? {1}'.format(n, flag)


# print(prime())


def all_primes():
    n = int(input("Enter a number: "))
    primes = []
    for i in range(2, n+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag == True:
            primes.append(i)
    return primes



# print(all_primes())


def min_max():
    List = []
    while True:
        n = input("Enter a number or 'q' to quit: ")
        if n == 'q':
            break
        elif n == '':
            continue
        List.append(eval(n))
    return 'max number is {}, min number is {}'.format(max(List), min(List))


# print(min_max())


def program6():
    x = int(input('Enter x> '))
    y = int(input('Enter y> '))
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
            print(hcf)

program6()





