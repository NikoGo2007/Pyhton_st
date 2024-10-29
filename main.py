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
    l = []
    d = []
    for i in range(int(n)):
        for j in range(int(m)):
            mtr += [random.randint(1, 100)]
        matrix.append(mtr)
        mtr = []
    print(*matrix, sep='\n')
    print("----------------")
    for i in matrix:
        l += [max(i)]
        d += [matrix.index(i)]
    k = d[l.index(max(l))]
    inn = matrix.index(matrix[k])
    mt = matrix[0:inn]+[matrix[k]]+matrix[inn:]
    return (mt)

#print(*i_8(int(input("колличество блоков ")),int(input("колличество столбцов "))),sep='\n')


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


def i_11(x_1={}, y_1={}, x_2={},key=""):
    if key == "а":
        z = {}
        # z = {**x, **y} способ в котором при повторении ключа будет браться значение из 2 словаря
        z.update(x_1)
        z.update(y_1)
        print(z)
    if key == "б":
        for i, b in x_2.items():
            print(i, b)
    if key == "в":
        a = {}
        k = [[1,23,4,5],[121,131,441,15],[12,2],[1212]]
        for m in k:
            a.update(dict.fromkeys((str(k.index(m)+1)), m))
        print(a)


a = {"a":1,"b":2}
b = {"c":3,"d":4}


#i_11(a,b,a,"в") #3 часть 11 задания #key это часть задания которую надо исполнить(русскими буквами)

def i_12(x_1, x_2, key=""):
    if key == "а":
        k_1 = 0
        a = tuple()
        for m in range(1, x_1 + 1):
            for k in range(1, int(input(f"количество строк в словаре {m} ")) + 1):
                k_1 += 1
                a += (dict.fromkeys(str(k_1), input(f"{k} строка в словаре {m} ")),)
        print(a)
    if key == "b":
        print(tuple(sorted(x_2, key=lambda x: isinstance(x, float))))

x = (21412, 214123.1, 142333, 12332.1231, 333333333333, 999999999999.1)

#i_12(int(input("количество словарей: ")), x, "а")


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

i_1 = {1,2,3,4}#первая строка
i_2 = {6,7,8,9}#вторая строка
i_3 = {1,3,5}#строка с помощью которой мы проверяем

#print(i_13_a(i_1, i_2, i_3))#1 часть 13 задания


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
            'skils': ["a", "B", "C"]
        }
    ],
    [
        {
            'id': 2,
            'skils': ["A", "B", "V"]
        }
    ],
    [
        {
            'id': 3,
            'skils': ["A", "B", "X"]
        }
    ],
    [
        {
            'id': 4,
            'skils': ["B", "A", "V"]
        }
    ],
]


print(i_13_b(lst))#2 часть 13 задания


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
