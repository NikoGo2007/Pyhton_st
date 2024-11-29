def SumRange(a, b):
    result = 0
    if a > b:
        return 0
    else:
        for i in range(a, b + 1):
            result += i
    return result


#print(SumRange(1,3)) #14 задание


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


#RemoveRows(10,10,[1,2]) #15 задание

def Digits(S):
    if not S:
        return 0
    if S[0].isdigit():
        return 1 + Digits(S[1:])
    else:
        return 0 + Digits(S[1:])

S = "a1b2c3d45"
result = Digits(S)
#print(result)



