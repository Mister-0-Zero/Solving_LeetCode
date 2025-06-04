class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(1, n):
            matrix[0][j] = 1

        for i in range(1, m):
            matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[-1][-1]

def print_m(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f" {matrix[i][j]} ", end = '')
        print()

instance = Solution()
res = instance.uniquePaths(4, 6)
print(res)
