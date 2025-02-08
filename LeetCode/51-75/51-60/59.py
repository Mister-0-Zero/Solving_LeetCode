class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        column, row = -1, 0
        dcol, drow = 1, 0

        for score in range(1, n * n + 1):
            column += dcol
            row += drow

            matrix[row][column] = score

            if column + dcol == n or row + drow == n or matrix[row + drow][column + dcol] != 0:
                dcol, drow = -drow, dcol

        return matrix

def print_m(matrix):
    print()
    print(" Matrix: ")
    for mass in matrix:
        for num in mass:
            print(f" {num} ", end="")
        print()
    print()

instance = Solution()
res = instance.generateMatrix(5)
print_m(res)
