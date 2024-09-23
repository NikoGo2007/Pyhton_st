m = "1234"


def main(i):
    if i == m:
        return "вы угадали"
    else:
        k = 0
        n = 0
        for j in i:
            k += m.count(j)
            if m in j:
                if m.index(j) == i.index(j):
                    n += 1
        return (f"Быки:{k}",f"Коровы:{n}")


i = input(": ")
if len(i) == 4:
    try:
        i = int(i)
        i = str(i)
        print(main(i))
    except ValueError:
        print("Не корректные данные")
else:
    print("Данные введены не корректно")

