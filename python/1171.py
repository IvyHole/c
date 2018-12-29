m,n=input().split()
m=int(m)
n=int(n)
i=1
sum=term=m
while i<=n:
    a=term/2
    if i==n:
        break
    else :
         sum=sum+2*a
    term=a
    i=i+1
print('%.2f'%a+' '+'%.2f'%sum)
