x=[int(i) for i in input().split()]
a=int(input())
if a in x:
    print(x.index(a))
if a not in x:
    print('Not exist!')
