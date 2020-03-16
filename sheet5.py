def sumN(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


# print(sumN(3))


def sumNCubes(n):
    sum = 0
    for i in range(n+1):
        sum += i**3
    return sum


# print(sumNCubes(3))


def fact():
    n = int(input("Enter a naumber: "))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


# print(fact())


def fibonaccii():
    n = int(input("Enter a number: "))
    a, b = 0, 1
    c = a + b
    list = [a, b]
    for i in range(n):
        list.append(c)
        a, b = b, c
        c = a + b
    return('fibonacci sequence: {0}\nnth fibonaccii number: {1}'.format(list, list[n-1]))


# print(fibonaccii())


def pi(t):
    x = 1
    y = 1
    sum = 0
    for i in range(t):
        sum += x/y
        x *= -1
        y +=2
    return 4*sum


print(pi(1000))
