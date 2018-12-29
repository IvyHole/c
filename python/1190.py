import math
def sw(a,b,c):
    return (a+b+c)/2
def area(a,b,c):
    s=sw(a,b,c)
    are=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return are

a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
areae=area(a,b,c)
print('%.3f'%areae)
