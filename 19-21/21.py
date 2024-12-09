f = open("matrices.txt", "r")
def sum_diagonals(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(len(matrix)):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][len(matrix) - i - 1]
    return main_diagonal_sum + secondary_diagonal_sum


two = open("21_2.txt", "w")
for i in f:
    print(i)
    print(sum_diagonals(i))
    if sum_diagonals(i) % 2 != 0:
        two.write(str(i) + "\n")
