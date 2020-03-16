# ----------------------------------- Revision Sheet Programs------------------------------------------------
# Note: I made all these programs on paper first :( then copied it here to check my output
# Another note: I used inputs given on the revision sheet

def SumMultiples(N, P):
    primes_list = []
    for i in range(2, N+1):
        flag = True # I could name it prime
        for j in range(2, i):
            if i%j == 0:
                flag = False
        if flag == True:
            primes_list.append(i)
    return sum(primes_list)*P


# print(SumMultiples(10, 7))


def RemNeg(L):
    new_list = [] # I didn't use remove because it will remove -1 and skip -2 :D
    for i in L:
        if i >= 0:
            new_list.append(i)
    return new_list


# print(RemNeg([1, 2, 3, -1, -2, 0]))

def ProgramCount(FName):
    fhand = open(FName)
    lines = fhand.readlines()
    fhand.close() # To save memory, we don't find memory in the street :D
    loop_cout = 0
    condition_count = 0
    for line in lines:
        line = line.strip()
        if line.startswith(('for', 'while')):
            loop_cout += 1
        if line.startswith(('if', 'elif')): # I don't think they count else as a condition so I make if and elif only
            condition_count += 1
    return 'loop_cout = {0}, condition_count = {1}'.format(loop_cout, condition_count)


# print(ProgramCount('Odd or Even.txt'))


def Intersec(D1,  D2):
    D3 = {}
    for i in D1:
        List = [] # Sorry I don't find any name but List :D
        if i in D2:
            List.append(D1[i])
            List.append(D2[i])
            D3[i] = List
    return D3

D1 = {1:'a', 2:'b', 3:'c'}
D2 = {2:'x', 4:'y', 1:'z'}
# print(Intersec(D1, D2))


def Round(n):
    i = n - int(n)                # def Round(n):
    if i >= 0.5:                  #     return round(n)   Done hahahaha
        return int(n)+1
    return int(n)

# print(Round(3.5))
# print(Round(2.2))


def ColAvg(F):
    fhand = open(F)
    lines = fhand.readlines()
    fhand.close()
    line1, line2, line3 = 0, 0, 0
    for line in lines:
        numbers = line.strip().split(',')
        line1 += int(numbers[0])
        line2 += int(numbers[1])
        line3 += int(numbers[2])
    return [line1/3, line2/3, line3/3] # I divided by 3 because he tells my each line is 3 integers, (note they returned as float but I can make them
                                       # integers as in the sheet's answer but if I changed the numbers it will give me wrong answer)

print(ColAvg('numbers.txt'))