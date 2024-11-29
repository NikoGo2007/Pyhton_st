def RemoveRows(m, n, k):
    strw = []
    matrx = []
    ma = []
    k0 = 0
    for i_n in range(n):
        for i_m in range(m):
            k0 += 1
            strw.append(k0)
        matrx.append(strw)
        print(strw)
        strw = []
    print("--------------------------")
    if k[0] > m:
        print(*matrx, sep="\n")
    elif k[1] > m:
        ma = matrx[:k[0] - 1] + matrx[m:]
    else:
        ma = matrx[:k[0] - 1] + matrx[k[1]:]
    print(*ma, sep="\n")


RemoveRows(10,10,[1,2])