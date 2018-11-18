a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a<b+c and b<a+c and c<b+a:
        if a==b or a==c or b==c:
            print("等腰三角形")
        elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b :
            print("直角三角形")
        else :
            print("一般三角形")
else:
    print("不能构成三角形")
    








    
 
