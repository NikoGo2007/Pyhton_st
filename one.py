import random
f = ["0","1","2","3","4","5","6","7","8","9"]
m = "" + str(random.randrange(1,10))
for i in range(10):
    s = random.choice(f)
    if s not in m:
        m += s
    if len(m) == 4:
        break
print(m)
def main(i):
    if i == m:
        return "вы угадали"
    else:
        k = 0
        n = 0
        for j in i:
            k += m.count(j)
            if j in m:
                if i.index(j) == m.index(j):
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

