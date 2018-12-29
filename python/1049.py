n=int(input())
r=[]
for i in range(n):
 r.append(1)
 for j in range(i-1,0,-1):
  r[j]+=r[j-1]
 for j in r:
  print(j, end=' ')
 print()
