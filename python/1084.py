num = [int(i) for i in input().split()]
num.remove(num[0])
x=[]
while len(num) > 0:
    number=num.pop()
    if number ==1:
        x.append(number)

print(len(x))
print('\r')
