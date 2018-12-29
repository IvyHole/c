li = input().split()
while len(li):
    print(['last', 'first'][min([int(x) for x in li]) % 2])
    li = input().split()
