n=int(input())

a=b='2'
i=1
sum=0
while i<=n:
    a=int(a)
    sum=sum+a
    a=str(a)
    a=a+b
    i=i+1

print(sum)
