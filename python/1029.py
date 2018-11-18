num = [int(n) for n in input().split()]
x=[]
y=[]
z=[]
while len(num) > 0:
    number=num.pop()
    if number >0 :
        x.append(number)
    elif number <0 :
        y.append(number)
    elif number == 0:
        z.append(number)

a=len(x)
b=len(y)
c=len(z)
print (a,b,c)
