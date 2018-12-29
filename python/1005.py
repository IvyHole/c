n=int(input())
i=1
c=[]
sum=[]
o=0
while (i<=n):
    num=[int(x) for x in input().split()]
    while len(num)>1:
        number=num.pop()
        c.append(number)

    for p in c:o=o+p
    sum.append(o)
    c=[]
    num=[]
    i=i+1
    o=0

for p in sum:print(p,end='\n')
