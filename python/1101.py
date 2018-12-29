import math
n=int(input())
p=pow(10,9)+1
sums=0
i=1
term=0
while i<=n:
    term=term+i
    sums=sums+term
    i=i+1
print("%.0f"%(sums%p))
