def summ(arg1, arg2):
    arg1.extend([0, ] * (len(arg2) - len(arg1)))
    arg2.extend([0, ] * (len(arg1) - len(arg2)))
    return list(map(sum, zip(arg1, arg2)))


def umn(arg1, arg2):
    if isinstance(arg2, int):
        result = []
        for i in arg1:
            result += [i * arg2]
        return result
    else:
        print("введите корректные данные")


def min_max(arg1, mi_ma):
    if mi_ma == "max":
        return arg1[arg1.index(max(arg1))]
    elif mi_ma == "min":
        return arg1[arg1.index(min(arg1))]
    else:
        return "Укажите верное действие"
