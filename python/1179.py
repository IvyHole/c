def mins (n,m):
    a=min([n,m])
    while 1==1:
        if n%a==0 and m%a==0:
            return a
        a=a-1

def maxs (n,m):
    b=max([n,m])
    while 1==1:
        if b%n==0 and b%m==0:
            return b
        b=b+1

n,m=input().split()
n=int(n)
m=int(m)
print(str(mins(n,m))+' '+str(maxs(n,m)))
