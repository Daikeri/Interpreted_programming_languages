import math
from random import randrange

# 1 variant 4
""""
time = int(input())
if time > 1440:
    hours = (time - 1440) // 60
    minutes = (time - 1440) % 60
    if hours == 24:
        hours = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    print(hours, minutes)
else:
    hours = time // 60
    minutes = time % 60
    if hours == 24:
        hours = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    print(hours, minutes)
"""

# 2 variant 5
"""
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
"""

# 3 variant 10

""""
n = int(input())
print(n // 10 % 10)
"""

# 4 variant 2

""""
a = int(input("a = "))
b = int(input("b = "))

if a < b:
    for i in range(a, b+1):
        print(i, end=" ")
else:
    for j in range(a, b-1, -1):
        print(j, end=" ")
"""

# 5 variant 7

"""
original = "STARThTytyPapahEND"
newStr = original[:(original.find("h"))] + original[(original.rfind("h"))+1:]
print(newStr)
"""

# 6 variant 15

"""
def Fibo():
    f_one = 0
    f_two = 1
    res = 0
    count = 2
    a = int(input())
    while res < a:
        res = f_one + f_two
        f_one = f_two
        f_two = res
        count += 1
    if res == a:
        print('Yes, FiboBebra n =', count)
    else:
        print(-1)
"""

# 7 variant 2

"""
n = 10
arr = [randrange(1, 20) for i in range(n)]
print(arr)

for i in arr:
    if i % 2 == 0:
        print(i, end=' ')
"""


# 8 variant 4

'''
def PowTail(number, grade):
    def Prom(numb, lvl, acc):
        if lvl > 0:
            acc *= numb
            lvl -= 1
            return Prom(numb, lvl, acc)
        else:
            return acc

    return Prom(number, grade, 1)


def PowUp(number, level):
    if level > 0:
        return PowUp(number, level - 1) * number
    else:
        return 1
'''

# 9 variant 6

'''
def GenerateMatrix():
    return [[randrange(1, 10) for i in range(11)] for i in range(3)]


def PrintMatrix(matrix):
    for first in matrix:
        for second in first:
            print(second, end=' ')
        print('\n')


def SwapMatrix(first, second, matrix):

    print('base matrix:')
    PrintMatrix(matrix)

    acc = []

    for fst in range(len(matrix)):
        acc.append(matrix[fst][first])

    for fst in range(len(matrix)):
        matrix[fst][first] = matrix[fst][second]

    for fst in range(len(matrix)):
        matrix[fst][second] = acc[fst]

    print('new matrix')
    PrintMatrix(matrix)

    return matrix


m = GenerateMatrix()

first = int(input('fst = '))
second = int(input('snd = '))
SwapMatrix(first, second, m)
'''

