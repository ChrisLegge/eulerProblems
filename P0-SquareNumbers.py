total = 0
for i in range(6*10**5):
    if (i*i)%2 != 0:
        total += (i*i)
print(total)