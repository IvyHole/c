import re

def getletter(n):
    c = re.sub(r'\W+','',n)
    c = re.sub(r'\d+','',c)
    return c

n=input()
print(getletter(n))
