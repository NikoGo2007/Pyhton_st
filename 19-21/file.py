f = open("21_1.txt", 'r')
k,m,ko,kj = [],[],[],[]
for i in f:
    if len(i) != 1:
        for mj in i.rstrip().split(" "):
            ko += [int(float(mj))]
        m += [ko]
        ko = []
    else:
        k += [m]
        m = []

for j in k:
    if j[0][0] == 0:
        kj += [k.index(j)]
print(*k, sep='\n')
print(kj)


two = open("21_test.txt", "a")
f2 = ""
flag = 1
flag2 = 0
l = []
for ind in kj:
    for i in k[ind]:
            for j in i:
                if flag == len(i):
                    if flag2 == len(k[ind]):
                        two.write("\n")
                        flag2 = 0
                    f2 += str(j) + " "
                    two.write(f2 + "\n")
                    f2 = ""
                    flag = 1
                    flag2 += 1
                else:
                    f2 += str(j) + " "
                    flag += 1