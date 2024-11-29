def summ(arg1, arg2):
    arg1.extend([0, ] * (len(arg2) - len(arg1)))
    arg2.extend([0, ] * (len(arg1) - len(arg2)))
    return list(map(sum, zip(arg1, arg2)))


a = [1,3,4,5]
b = [1,2,3]


def umn(arg1, arg2):
    result = []
    for i in arg1:
        result += [i * arg2]
    return result


def min_max(arg1, mi_ma):
    if mi_ma == "max":
        return arg1[arg1.index(max(arg1))]
    elif mi_ma == "min":
        return arg1[arg1.index(min(arg1))]
    else:
        return "ERROR"

print(min_max(a,"mm"))