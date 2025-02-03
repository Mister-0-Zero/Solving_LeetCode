class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        n_, m_ = 0, 0
        res = []
        for number_circle in range(min(n // 2 if n / 2 % 2 == 0 else n //2 + 1,\
                                       m // 2 if m / 2 % 2 == 0 else m //2 + 1)):
            mass_range = [[number_circle, m - number_circle], [1 + number_circle, n - number_circle], [m - 2 - number_circle, -1 + number_circle], [n - 2 - number_circle, 0 + number_circle]]
            mass_ind = [[number_circle, -1], [-1, m - 1 - number_circle], [n - 1 - number_circle, -1], [-1, number_circle]]

            for i in range(4):
                for j in range(mass_range[i][0], mass_range[i][1], 1 if i <= 1 else -1):
                    res.append(matrix[mass_ind[i][0] if mass_ind[i][0] != -1 else j][mass_ind[i][1] if mass_ind[i][1] != -1 else j])
                if i % 2 == 0:
                    n_ +=1
                    if n_ == n: break
                else:
                    m_ +=1
                    if m_ == m: break

            # for j in range(number_circle, m - number_circle):
            #     res.append(matrix[number_circle][j])
            # n_ += 1
            # if n_ == n: break
            # for i in range(1 + number_circle, n - number_circle):
            #     res.append(matrix[i][m - 1 - number_circle])
            # m_ += 1
            # if m_ == m: break
            # for j in range(m - 2 - number_circle, -1 + number_circle, -1):
            #     res.append(matrix[n - 1 - number_circle][j])
            # n_ += 1
            # if n_ == n: break
            # for i in range(n - 2 - number_circle, 0 + number_circle, -1):
            #     res.append(matrix[i][number_circle])
            # m_ += 1
            # if m_ == m: break

        return res



def print_m(matrix):
    for mass in matrix:
        for num in mass:
            print(f" {num} ", end="")
        print()
    print()

instance = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
print_m(matrix)

res = instance.spiralOrder(matrix)
print(res)