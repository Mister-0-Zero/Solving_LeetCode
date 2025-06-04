import random

def print_m(matrix):
    print()
    for row in matrix:
        print(" ".join(f"{x:2}" for x in row))
    print()

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        matrix = grid
        matrix_res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        matrix_res[0][0] = matrix[0][0]

        for i in range(1, len(matrix)):
            matrix_res[i][0] = matrix[i][0] + matrix_res[i - 1][0]

        for j in range(1, len(matrix[0])):
            matrix_res[0][j] = matrix[0][j] + matrix_res[0][j -1]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix_res[i][j] = matrix[i][j] + min(matrix_res[i - 1][j], matrix_res[i][j -1])

        return matrix_res[-1][-1]

n, m = random.randint(2, 5), random.randint(2, 5)
matrix = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]

print_m(matrix)  # Исходная матрица
instance = Solution()
res = instance.minPathSum(matrix)

print("Число уникальных путей:", res)