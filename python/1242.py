n = int(input())
li = []
for i in range(n // 2):
    li.append(' ' * i + '*' * (n - i * 2))
    li.append(' ' * i + '*' * (n - i * 2))
li.append(' ' * (n // 2) + '*')

print('\n'.join(li))
print('*' * (3 * n))
li.reverse()
print('\n'.join(li))
