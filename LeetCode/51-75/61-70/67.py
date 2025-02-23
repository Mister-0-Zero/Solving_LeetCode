class Solution:
    def addBinary(self, a: str, b: str) -> str:
        score = 0
        for ind, val in enumerate(a[::-1]):
            score += int(val) * 2 ** ind
        for ind, val in enumerate(b[::-1]):
            score += int(val) * 2 ** ind
        return bin(score)[2:]

instance = Solution()
a, b = '101', '1'
res = instance.addBinary(a, b)
print(res)