class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = int(str(abs(x))[::-1]) * -1
        else:
            res = int(str(x)[::-1])
        if abs(res) < 2 ** 31:
            return res
        else:
            return 0

ex = Solution()
print(ex.reverse(-123044444444444444444444444444444444450000))