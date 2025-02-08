class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)] #формируем матрицу нулей
        column, row = -1, 0
        dcol, drow = 1, 0

        for score in range(1, n * n + 1):
            column += dcol
            row += drow

            matrix[row][column] = score

            if column + dcol == n or row + drow == n or matrix[row + drow][column + dcol] != 0:
                dcol, drow = -drow, dcol #суть просто, идем до конца строки или столбца или до заполнилненого поля
                #а потом меняем направление движения, чтобы идти дальше по часовой стрелке

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
