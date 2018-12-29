a=[int(i) for i in input().split()]
b=int(input())
a.append(b)
a.sort()
for i in a:print(i,end='\n')
