for i in range(1,10):
    result=[]
    for j in range(1,i+1):
        result.append(j)
    for j in range(i-1,0,-1):
        result.append(j)
    result=''.join(str(x) for x in result)
    print("{0:^17}".format(result))
