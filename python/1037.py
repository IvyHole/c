n=int(input())
i=1
b=[]
w=[]
h=[]
sum1=0
while i<=n:
    ba,wa,ha=input().split()
    ba=int(ba)
    wa=int(wa)
    ha=int(ha)
    b.append(ba)
    w.append(wa)
    h.append(ha)
    i=i+1

for j in range(n):
    b1=b[j]
    w1=w[j]
    h1=h[j]
    i=n-1
    while j<i:
        bb=b[i]
        wb=w[i]
        hb=h[i]
        if(b1<bb and w1<wb and h1<hb):
            sum1=sum1+1
        i=i-1
print(sum1)
