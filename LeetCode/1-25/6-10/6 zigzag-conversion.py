class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        mass = ['' for _ in range(numRows)]
        ind = 0
        for sim in s:
            if ind == numRows - 1: direction = False
            elif ind == 0: direction = True
            mass[ind] += sim
            ind = ind + 1 if direction else ind - 1
        return ''.join(mass)

exepl = Solution()
s = 'aaaabs'
numRows = 2
print(exepl.convert(s, numRows))
