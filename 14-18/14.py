def SumRange(a, b):
    result = 0
    if a > b:
        return 0
    else:
        for i in range(a, b + 1):
            result += i
    return result


print(SumRange(7,5))