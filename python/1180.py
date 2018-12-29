def sf (n):
    a=n
    sf=[]
    while a>=0:
        if n%a==0:
            sf.append(a)
        a=a-1

    if len(sf) == 2:
        return 0
    else :
        return 1

n=int(input())
if sf(n) == 0:
    print('prime')
else:
    print('not prime')
