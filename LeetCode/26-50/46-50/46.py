class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def f(n,  res = None):
            if res is None:
                res = []
            if n == len(nums):
                res.append(nums[:])
            for i in range(n, len(nums)):
                nums[n], nums[i] = nums[i], nums[n]
                f(n + 1,  res)
                nums[n], nums[i] = nums[i], nums[n]
            return res

        return f(0)

instance = Solution()
res = instance.permute([1, 2, 3])
print(res)