import copy
from time import time

c = time()
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_ = []
        for list in board:
            list_ = []
            for x in list:
                list_.append(int(x) if x!="." else 0)
            board_.append(list_)
        board = board_

        for i in range(9):
            mass_check = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            for j in range(9):
                if mass_check[board[i][j]] == 0:
                    return False
                mass_check[board[i][j]] -= 1

        for i in range(9):
            mass_check = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            for j in range(9):
                if mass_check[board[j][i]] == 0:
                    return False
                mass_check[board[j][i]] -= 1


        paramI = 0
        for _ in range(3):
            paramJ = 0
            for _ in range(3):
                mass_check = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                for i in range(paramI, paramI + 3):
                    for j in range(paramJ, paramJ + 3):
                        if mass_check[board[i][j]] == 0:
                            return False
                        mass_check[board[i][j]] -= 1
                paramJ += 3
            paramI += 3
        return True

instance = Solution()
for i in range(100):
    res = instance.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],["3",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],\
     ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],\
     [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    )
    if i == 9: print(res)
    res = instance.isValidSudoku(
    [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],\
     ["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],\
     [".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    )
    if i == 9: print(res)
    res = instance.isValidSudoku(
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],\
         ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],\
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    )
    if i == 9: print(res)
print(c - time())
print()

c = time()

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        n = len(board)
        dict_digit = {}

        for i in range(1, 10):
            dict_digit[str(i)] = 1
        dict_digit["."] = 10**10

        for i in range(n):
            dict_check = copy.copy(dict_digit)
            for j in range(n):
                if dict_check[board[i][j]] == 0:
                    return False
                dict_check[board[i][j]] -= 1


        for i in range(n):
            dict_check = copy.copy(dict_digit)
            for j in range(n):
                if dict_check[board[j][i]] == 0:
                    return False
                dict_check[board[j][i]] -= 1

        paramI = 0
        for _ in range(3):
            paramJ = 0
            for _ in range(3):
                dict_check = copy.copy(dict_digit)
                for i in range(paramI, paramI + 3):
                    for j in range(paramJ, paramJ + 3):
                        if dict_check[board[i][j]] == 0:
                            return False
                        dict_check[board[i][j]] -= 1

                paramJ += 3
            paramI += 3
        return True

instance = Solution()
for i in range(100):
    res = instance.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."],["3",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],\
     ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],\
     [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    )
    if i == 9: print(res)
    res = instance.isValidSudoku(
    [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],\
     ["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],\
     [".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    )
    if i == 9: print(res)
    res = instance.isValidSudoku(
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],\
         ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],\
         [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    )
    if i == 9: print(res)
print(c - time())
print()
