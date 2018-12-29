n=int(input())
i=1
su=[]
sp=[]
sums=[]
while i<=(2*n-2):
    a=input()
    a1=list(a)
    su.extend(a1)
    i=i+1
su1=su   
mina=min(su)
minai=mina
num=su.count(mina)
for i in range(len(su)):
    if mina in su:
        qq=su[i]
        sp.append(qq)
        su.remove(mina)

for p in range(2*n-2):
    if p-1 in su1:
        sums.append('P')
    else:
        sums.append('S')

for t in sums: print(t,end='')
