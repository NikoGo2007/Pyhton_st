import numpy as np
one = open("21_1.txt", "r")
k,m,ko = [],[],[]
for i in one:
    print(len(i))
    if len(i) != 1:
        for mj in i.rstrip().split(" "):
            ko += [int(mj)]
        m += [ko]
        ko = []
    else:
        k += [m]
        m = []
print(k)

def sum_diagonals(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(len(matrix)):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][len(matrix) - i - 1]
    return main_diagonal_sum + secondary_diagonal_sum


two = open("21_2.txt", "w")
f2 = ""
flag = 1
flag2 = 0
l = []
for i in k:
    if sum_diagonals(i) % 2 != 0:
        l += [k.index(i)]
        for x in i:
            for y in x:
                if flag == len(x):
                    if flag2 == len(x):
                        two.write("\n")
                        flag2 = 0
                    f2 += str(y) + " "
                    two.write(f2 + "\n")
                    f2= ""
                    flag = 1
                    flag2 += 1
                else:
                    f2 += str(y) + " "
                    flag += 1

tree = open("21_3.txt", "w")
f2 = ""
flag = 1
flag2 = 0
l = []
for i in k:
    if sum_diagonals(i) % 2 == 0:
        for x in i:
            for y in x:
                if flag == len(x):
                    if flag2 == len(x):
                        tree.write("\n")
                        flag2 = 0
                    f2 += str(y) + " "
                    tree.write(f2 + "\n")
                    f2= ""
                    flag = 1
                    flag2 += 1
                else:
                    f2 += str(y) + " "
                    flag += 1

    else:
        all = np.array(i).transpose()
        for x in all:
            for y in x:
                if flag == len(x):
                    if flag2 == len(x):
                        tree.write("\n")
                        flag2 = 0
                    f2 += str(y) + " "
                    tree.write(f2 + "\n")
                    f2= ""
                    flag = 1
                    flag2 += 1
                else:
                    f2 += str(y) + " "
                    flag += 1
