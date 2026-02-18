#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import math

a = 999
b = 999
palendrome = False
value = 0

def isPaldendrome(num):
    numArr = list(map(int, str(num)))
    for i in range(math.floor(len(numArr)/2)):
        if len(numArr) == 0:
            return False
        else:
            if numArr[0] == numArr[len(numArr)-1]:
                numArr.pop(0)
                if len(numArr) != 0:
                    numArr.pop(len(numArr)-1)
            else:
                return False
    return True

while palendrome == False:
    if isPaldendrome(a*b):
        if a*b > value:
            value = a*b
    else:
        a -= 1
        if a == 0:
            b -= 1
            a = 999
            if b == 0:
                palendrome = True
print(a, b, value)