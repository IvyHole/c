n=int(input())
x=[]
num = [int(i) for i in input().split() ]
x.append(max(num))
x.append(min(num))
for t in x:print (t,end=" ")     

