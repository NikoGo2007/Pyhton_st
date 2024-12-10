f = open("test.txt", "r")
k,m,ko = [],[],[]
for i in f:
    if len(i) != 1:
        for mj in i.rstrip().split(" "):
            ko += [int(float(mj))]
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
for i in k:
    print(i)
    print(sum_diagonals(i))
    if sum_diagonals(i) % 2 != 0:
        two.write(str(i) + "\n")
