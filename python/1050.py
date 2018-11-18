x=int(input())
a=x%4
b=x%100
if a==0 and b==0:
    print('yes')
elif a==0 and b!=0:
    print('yes')
else:
    print('no')
