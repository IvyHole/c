import math
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a>abs(b-c)and b>abs(a-c) and c>abs(a-b) :
        p=(a+b+c)/2.0
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print('%.6f'%s)
    else:
        print("This is not a valid triangle!")
	
else :
    print("This is not a valid triangle!")
