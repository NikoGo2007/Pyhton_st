#imports
import math
from tabulate import tabulate
import random


def i_1(x):
    x = int(x)
    y = ((1 / 2) * (int(x) ** 2)) - (3 * int(x)) + 1
    m = f"Функция y имеет занчение: {str(y)} при х равном: {str(x)}"
    return m


#print(i_1(input("x ")))


def i_2(t):
    t = int(t)
    return (t - 32) * (5 / 9)


#print(i_2(input("Значение температуры в  фаренгейтах")))


def i_3(x):
    x = int(x)
    y = math.cos(2 * x - 1) if x > 2 else math.sin(3 * x - 1)
    return y


#print(i_3(input("x")))


def i_4(a, b):
    m = 1
    for i_a in range(a, b + 1):
        m *= i_a
    return m


#print(i_4(int(input("a: ")), int(input("b: "))))


def i_5(n):
    n = int(n)
    m = 0
    for i in range(1, n + 1):
        m += ((-1) ** (n + 1)) * math.factorial(int(i))
    return m


#print(i_5(input("n ")))


def i_6(x):
    k = []
    j = []
    for i in range(0, len(x)):
        if x[i] == max(x) or x[i] == min(x):
            k += [i]
    for i in range(1, abs(k[0] - k[1])):
        j += [0]

    n = x[0:k[0] + 1] + j + x[k[1]:len(x)]
    return (n)


#print(i_6([1351,144,1,22,33,21,36,2]))


def i_7(n, k):
    l = []
    for i in range(0, len(n)):
        if n[i] < k:
            l += [n[i]]
    l = sorted(l)
    return l


#print(i_7([1,2,3,4,5,6,7,8,9,-1,10,11,12,13,14,15], 2))


def i_8(n, m):
    import random
    matrix = []
    mtr = []
    k = 0
    for i in range(int(n)):
        for j in range(int(m)):
            mtr += [random.randint(1, 100)]
        matrix.append(mtr)
        mtr = []
    print(*matrix, sep='\n')
    return max(matrix)

print(i_8(int(input("колличество блоков ")),int(input("колличество столбцов "))))


def i_9(n):
    return (" ".join(n.split()))


#print(i_9(input("Введите предложение с избыточными пробелами: ")))


def i_10(n):
    l = ""
    for i in range(len(n)):
        if i % 2 == 0:
            l += n[i]
    return l

#print(i_10(input("строка ")))


def i_11_a(x, y):  #1 часть задания 11
    z = {}
    # z = {**x, **y} способ в котором при повторении ключа будет браться значение из 2 словаря
    z.update(x)
    z.update(y)
    return z


#print(i_11_a({"a":1,"b":2}, {"c":3,"d":4}))

#print(tabulate({"a":1,"b":2,"c":3}.items())) #2 часть 11 задания


def i_11_b(x):
    a = {}
    for m in range(1, x + 1):
        k = list(input(f"список {m} "))
        a.update(dict.fromkeys(str(m), k))
    return a


#print(i_11_b(int(input("колличество списков < 10 ")))) #3 часть 11 задания


def i_12_a(x):
    k_1 = 0
    a = tuple()
    for m in range(1, x + 1):
        for k in range(1, int(input(f"колличество строк в словаре {m} ")) + 1):
            k_1 += 1
            a += (dict.fromkeys(str(k_1), input(f"{k} строка в словаре {m} ")),)
    return a


#print(i_12_a(int(input("колличество словарей "))))  #1 часть задания 12


x = (21412, 214123.1, 142333, 12332.1231, 333333333333, 999999999999.1)


#print(tuple(sorted(x, key=lambda x: isinstance(x, float)))) #2 часть задания 12


def i_13_a(x, y, z):
    k = 0
    result = x.union(y)
    print(result)
    for i in result:
        if i in z:
            k += 1
    if k == len(z):
        return "могут"
    else:
        return "не могут"


#print(i_13_a({1,2,3,4,5},{6,7,8,9}, {3,5,10}))#1 часть 13 задания


def i_13_b(lst):
    skils = []
    f = []
    for u in range(len(lst)):
        for j in lst[u]:
            skils += (j["skils"])
    for m in skils:
        if skils.count(m) == 1:
            f += [m]
    return f


lst = [
    [
        {
            'id': 1,
            'skils': ["1Ab", "2bC", "3"]
        }
    ],
    [
        {
            'id': 2,
            'skils': ["1Ab", "2bC", "c"]
        }
    ],
    [
        {
            'id': 3,
            'skils': ["1Ab", "2bC", "3c"]
        }
    ],
    [
        {
            'id': 4,
            'skils': ["1Ab", "2bC", "C1"]
        }
    ],
]


#print(i_13_b(lst))#2 часть 13 задания


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
