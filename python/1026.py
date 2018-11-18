sum=0
a=2
b=1
i=1
while (i<=20) :
    term=a/b
    sum=sum+term
    c=a+b
    b=a
    a=c
    i=i+1

print("%.2f"%sum)
