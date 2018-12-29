n=int(input())
ls=[int(i) for i in input().split()]
i=1
q=0

while 1==1:
    a1=min(ls)
    ls.remove(a1)
    a2=min(ls)
    ls.remove(a2)
    q=q+a2-a1
    if len(ls)==0:
        break
print(q)
