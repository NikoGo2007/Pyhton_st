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

#i_12(int(input("количество словарей: ")), x, "b")


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

i_1 = {1,2,3,4,5}#первая строка
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

