#project calc
from numbers_in_words import text, action, num_20_1, num_100_10


def calc(arg1, arg2, action_):
    if action_ == action[0]:
        return arg1 + arg2
    elif action_ == action[1]:
        return arg1 - arg2
    elif action_ == action[2] or action_ == action[3]:
        return arg1 / arg2
    elif action_ == action[4]:
        return arg1 * arg2


def determinat(arg):
        if arg in num_20_1[0]:
            for i in num_20_1[0]:
                if arg == i:
                    return [(num_20_1[1][num_20_1[0].index(i)]), 1]
        elif arg in num_100_10[0]:
            for i in num_100_10[0]:
                if arg == i:
                        return [(num_100_10[1][num_100_10[0].index(i)]), 2]
        elif arg in action:
            for i in action:
                if arg == i:
                        return [arg, 3]


f = input(": ").split()
flag = 0
arg1 = 0
arg2 = 0
action_ = ""
for i in f:
    if i == "на":
        None
    else:
        if determinat(i):
            g = determinat(i)
            if isinstance(g[0], int):
                if flag <= 3:
                    arg1 += g[0]
                    flag += g[1]
                elif flag >= 4:
                    arg2 += g[0]
                    flag += g[1]
            else:
                action_ = g[0]
                flag += g[1]
if action_ and arg1 and arg2:
    res = calc(arg1, arg2, action_)
    print(res)
else:
    print("Данные введены не корректно")

