t=int(input())
i=1
N=97
d=0
h=1
sums=[]
ai=[]
while(i<=t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    if n>26: ki=122
    else: ki=k+96
    p=n/k
    if n%k!=0:
        o=n%k
        sue=0
    else:
        o=0
        sue=1
    while (1==1):
        if sue==1:
            while(h<=p):
                ai.append(chr(N+d))
                h=h+1
            if d==(k-1):
                break
            d=d+1
            h=1
        else:
            h=h-o
            while(h<=p):
                ai.append(chr(N+d))
                h=h+1
            if d==k:
                break
            d=d+1
            h=1
            sue=1
        
        h=1
    aii=''.join(ai)
    sums.append(aii)
    i=i+1
    d=0
    ai=[]
    h=1
for j in sums: print(j,end='\n')
