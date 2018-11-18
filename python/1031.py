num = [int(n) for n in input().split()]
x=[]
while len(num) > 0 :
    a=min(num)
    x.append(a)
    num.remove(min(num))

for i in x : print(i,end=' ')
