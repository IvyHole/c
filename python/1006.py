i=1
c=[]
sum=[]
o=0
while (i==1):
    num=[int(x) for x in input().split()]
    while len(num)>1:
        number=num.pop()
        c.append(number)

    for p in c:o=o+p
    sum.append(o)
    for p in sum:print(p,end='\n')
    c=[]
    num=[]
    o=0
    sum=[]
