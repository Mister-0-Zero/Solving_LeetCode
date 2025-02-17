def print_m(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f" {matrix[i][j]} ", end = '')
        print()