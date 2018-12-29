a=int(input())
n=[int(i) for i in input().split()]
c=int(input())
i=1
l=[]
while i<=c:

    q=n.pop()
    l.append(q)

    i=i+1
n.reverse()

n.extend(l)
n.reverse()

for i in n:print(i,end=' ')

