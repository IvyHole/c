import math
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
i=1
sum1=sum2=sum3=0
while i<=(a) :
    sum1=sum1+i
    i=i+1

i=1
while i<=(b):
    sum2=sum2+pow(i,2)
    i=i+1

i=1
while i<=(c):
    sum3=sum3+1/i
    i=i+1
print('%.2f'%(sum1+sum2+sum3))
