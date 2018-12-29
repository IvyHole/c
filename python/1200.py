n=int(input())
m=input()
c=int(input())
m=list(m)
g=[]
def sss(b,c):
    j=[]
    while len(b)>=c:
        a=b.pop()
        j.append(a)
    j.reverse()
    return j


g=sss(m,c)
print(''.join(g))
