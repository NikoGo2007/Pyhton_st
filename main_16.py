#Задание 16 -----------------------------------------------------------------
def one(x, y, arg=False):
    if len(x) == len(y):
        if arg:
            return arg(x, y)
        else:
            return (*x, *y)
    else:
        return "Некорректные данные"


def krit(n1, m1):
    l = []
    for i0 in range(0, len(n1)):
        for i1 in range(0, len(m1)):
            if n1[i0] % 2 == 0 and m1[i1] % 2 == 0:
                l.append((n1[i0], m1[i1]))
    return l


#print(one([1,2,3,4],[5,6,7,8], krit)) #1 часть 16 задания ------------------


def two(x, arg=" "):
    l = ""
    for i in range(0, len(x)):
        l += x[i] + arg
    return l


a = ["abcd", "hnhffvdsc", "dffddfdv", "sdfsdfs"]


#print(two(a,":|:")) #2 часть 16 задания ------------------------------------


def three(j):
    l = []
    for i in j:
        l += [i.upper()]
    return l
#print(three(a)) #3 часть 16 задания ----------------------------------------
