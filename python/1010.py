n=1
sum=[]
while 1==1:
    num=[int(i) for i in input().split()]
    if num[0]==0:
        break
    a=num[0]
    while n<=a:
        x1=num.pop()
        x2=num.pop()
        x3=x1+x2
        sum.append(x3)
        n=n+1
    sum.reverse()
    for i in sum: print(i,end=' ')
    print('')
    num=[]
    n=1
    sum=[]
