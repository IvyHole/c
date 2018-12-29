m=100000007
while 1==1:
    n,p=map(int,input().split(' '))
    ans=1
    while p>0 :
        if(p%2==1):
            ans=ans*n%m
        p=p // 2
        n=n*n%m
    print (ans)
