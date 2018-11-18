n=int(input())
i=0
l=3
x=1
y=1
while (i<n) :
    if n!=1 and n!=2:
        z=x
        x=x+y
        y=z
        i=i+l
        l=1
    else:
        i=i+1

print (x)
   
    
