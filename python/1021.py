x=int(input())
a=int(x/1000)
b=int((x-a*1000)/100)
c=int((x-a*1000-b*100)/10)
d=x%10
print(d*1000+c*100+b*10+a)
