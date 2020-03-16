import math


def temp():
    fahrenheit_temp = eval(input("Enter fahrenheit_temp: "))
    celsius_temp = (fahrenheit_temp-32)*(5/9)
    return celsius_temp


print(temp())


def distance():
    kilometres = eval(input("Enter kilometres: "))
    miles = kilometres*0.62
    return miles


print(distance())


def weight():
    kilo = eval(input("Enter kilos: "))
    Weight = kilo*9.8
    return Weight


print(weight())


def roots():
    a, b, c = eval(input('Enter a, b, c: '))
    root1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    root2 = (-b-math.sqrt(b**2-4*a*c))/2*a

    return root1, root2

print(roots())

def area():
    a, b, c = eval(input('Enter a, b, c: '))
    s = 0.5*(a+b+c)
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return Area

print(area())
