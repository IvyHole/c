
import math
n=int(input())
a = 2
b = 1
c = a / b
l = []
for i in range(n):
    c = a / b
    a = a + b
    b = a - b
    l.append(c)
print('%.2f'%sum(l))
