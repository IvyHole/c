n=int(input())
m=[]
for i in range(n):
    b=0
    p=1
    a=int(input())
    while 1==1:
        p=p*2
        b=b+1
        if p>=a:
            break;
    m.append(b)
for p in m:print(p,end='\n')
