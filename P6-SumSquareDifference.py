sum = 0
squ = 0
for i in range(1, 101):
    sum += i**2
for i in range(1, 101):
    squ += i
print((squ**2)-sum)