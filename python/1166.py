n=int(input())
term=1
i=1
sum=0
while i<=n:
    term*=i
    sum+=term
    i=i+1
print(sum)
