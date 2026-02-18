a = 1
b = 2
total = 0
while b < 4*10**6:
    temp = b
    b = a+b
    a = temp
    if temp%2 == 0:
        total += temp
print(total)