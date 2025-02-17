import random

def print_m(matrix):
    print()
    for row in matrix:
        print(" ".join(f"{x:2}" for x in row))
    print()


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        matrix = obstacleGrid

        matrix = [[-cell for cell in row] for row in matrix]

        if matrix[0][0] == -1 or matrix[-1][-1] == -1:
            return 0

        matrix[0][0] = 1

        # Заполняем первую колонку
        for i in range(1, len(matrix)):
            if matrix[i][0] == -1:
                break
            matrix[i][0] = 1

        # Заполняем первую строку
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == -1:
                break
            matrix[0][j] = 1

        # Заполняем остальную матрицу
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == -1:
                    continue  # Если препятствие, пропускаем
                if matrix[i - 1][j] != -1:
                    matrix[i][j] += matrix[i - 1][j]
                if matrix[i][j - 1] != -1:
                    matrix[i][j] += matrix[i][j - 1]

        print_m(matrix)  # Итоговая матрица
        return matrix[-1][-1]

# Генерация случайной карты с препятствиями
n, m = random.randint(2, 5), random.randint(2, 5)
while True:
    matrix = [[int(random.randint(1, 100) > 80) for _ in range(m)] for _ in range(n)]
    if matrix[0][0] == 0:  # Начальная позиция не должна быть препятствием
        break

print_m(matrix)  # Исходная матрица
instance = Solution()
res = instance.uniquePathsWithObstacles(matrix)

print("Число уникальных путей:", res)
