class Solution:
    def climbStairs(self, n: int) -> int:

        def factorial(n):
            res = 1
            for i in range(2, n + 1):
                res *= i
            return res

        if n == 1:
            return 1

        kol_step = 1
        max_kol_two = n // 2

        for k in range(1, max_kol_two + 1):
            n_ = n - k
            kol_step += factorial(n_) / (factorial(k) * factorial(n_ - k))

        return kol_step

instance = Solution()
res = instance.climbStairs(4)
print(res)
