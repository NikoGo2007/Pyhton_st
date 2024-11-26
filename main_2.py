def SumRange(a, b):
    result = 0
    if a > b:
        return 0
    else:
        for i in range(a, b + 1):
            result += i
    return result


#print(SumRange(1,18)) #14 задание

def RemoveRows(m, n, k):
    strw = []
    matrx = []
    k0 = 0
    if m >= k[1]:
        for i_n in range(n):
            for i_m in range(m):
                k0 += 1
                strw.append(k0)
            matrx.append(strw)
            strw = []
    ma = matrx[:k[0] - 1] + matrx[k[1]:]
    for j in ma:
        print(j)
#RemoveRows(10,10,[2,6]) #15 задание