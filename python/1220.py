a,b,c=input().split('')
a=float(a)
b=float(b)
c=float(c)
if a+b>c and a+c>b and b+c>a :
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('%0.6f' %area)
else:
    print('This is not a valid triangle!')
