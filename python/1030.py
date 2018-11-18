n=40
i=0
l=3
x=1
y=1
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
while (i<n) :
    if n!=1 and n!=2:
        z=x
        x=x+y
        y=z
        i=i+l
        l=1
    else:
        i=i+1
    if i<=8 :
        x1.append(x)
    elif 8<i<=16 :
        x2.append(x)
    elif 16<i<=24:
        x3.append(x)
    elif 24<i<=32:
        x4.append(x)
    elif 32<i<=40:
        x5.append(x)
        
for t in x1: print(t, end=' ')
print()
for t in x2: print(t, end=' ')
print()
for t in x3: print(t, end=' ')
print()
for t in x4: print(t, end=' ')
print()
for t in x5: print(t, end=' ')

