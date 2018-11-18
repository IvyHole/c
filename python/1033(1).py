matrix = [input().split() for i in range(3)]
rev = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print('\n'.join([' '.join(x) for x in rev]))
