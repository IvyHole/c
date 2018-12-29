while 1==1:
    x=int(input())
    if 0<=x<=14:
        print("%.2f"%(x*6))
    elif 15<=x<=500:
        print("%.2f"%(x*(6-0.1)))
