def zun(a,b,c):
    x=[]
    y=[]
    z=[]
    x.append(a.pop())
    x.append(b.pop())
    x.append(c.pop())
    y.append(a.pop())
    y.append(b.pop())
    y.append(c.pop())
    z.append(a.pop())
    z.append(b.pop())
    z.append(c.pop())
    for i in z:print(i,end=' ')
    print('')
    for i in y:print(i,end=' ')
    print('')
    for i in x:print(i,end=' ')
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
zun(a,b,c)
