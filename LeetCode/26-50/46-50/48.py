from copy import deepcopy

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrix_ = deepcopy(matrix)
        for j in range(len(matrix)):
            for i in range(len(matrix)):
                current = matrix_[i][j]
                matrix[j][len(matrix) - 1 - i] = current
        return matrix

def print_m(matrix):
    for mass in matrix:
        for num in mass:
            print(f" {num} ", end = "")
        print()
    print()

instance = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_m(matrix)

res = instance.rotate(matrix)




print_m(res)