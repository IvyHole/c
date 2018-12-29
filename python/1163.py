num=[int(i) for i in input().split()]
a=num[0]
b=num[1]
x=max(num)
y=min(num)
v=[]
while 1==1:
    if a%y==0 and b%y==0:
        v.append(y)
        break
    else:
        y=y-1

while 1==1:
    if x%a==0 and x%b==0 :
        v.append(x)
        break
    else:
        x=x+1

for p in v: print(p,end=' ')
