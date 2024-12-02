def RemoveRows(matrix, k):
    if k[0] > len(matrix):
        return matrix
    elif k[1] > len(matrix):
        ma = matrix[:k[0] - 1] + matrix[len(matrix):]
    else:
        ma = matrix[:k[0] - 1] + matrix[k[1]:]
    return ma


mtrx = [[1,2,3,4,5],[6,7,8,9,0],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]

print(*RemoveRows(mtrx,[2,4]), sep="\n")