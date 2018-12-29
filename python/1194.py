n=[str(p) for p in input().split()]
m=[]
for j in n:
    i=ord(j)
    i=i+1
    if  i==123:
        i=ord('a')
    if i==91:
        i=ord('A')
    m.append(chr(i))

for o in m:print(o,end=' ')
