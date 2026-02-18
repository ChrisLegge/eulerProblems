#import math
#ans = 0
#for num in range(3, 600851475143, 2):
#    if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
#        if 600851475143%num == 0:
#            ans = num
#print(ans)

n = 600851475143
factor = 2
while factor * factor <= n:
    if n % factor == 0:
        n //= factor
    else:
        factor += 1 if factor == 2 else 2  # skip even numbers
print(n)