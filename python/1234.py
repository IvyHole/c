n=input()
m=input()
n=list(n)
print(n)
while m in n:
    n.remove(m)
    print(n)
for i in n:print(i,end='')
