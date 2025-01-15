class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "": return 0
        res = ''
        znak = 1
        if s[0] == '-':
            znak = -1
            s = s.replace('-', '', 1)
        elif s[0] == '+':
            s = s.replace('+', '', 1)
        for sim in s:
            if sim.isdigit():
                res += sim
            else:
                break
        if res == '': return 0
        res = int(res)
        res *= znak
        if res < -2 ** 31: return -2 ** 31
        if res > 2 ** 31 - 1: return 2 ** 31 - 1
        return res

ex = Solution()
s = "   -042"
print(ex.myAtoi(s))