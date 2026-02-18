#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import math

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

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        product = a * b
        if product > value and isPaldendrome(product):
            value = product

print(value)