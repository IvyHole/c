import re

def getchar(m):
    k=re.findall(r' ',m)
    l=re.findall(r'[a-zA-Z]',m)
    n=re.findall(r'[0-9]',m)
    f=re.sub(r'\w','',m)
    f=re.sub(r' ','',f)
    k=list(k)
    l=list(l)
    n=list(n)
    f=list(f)
    sum=[len(l),len(n),len(k),len(f)]
    return sum
m=input()
rsum=getchar(m)
for i in rsum:print(i,end=' ')
