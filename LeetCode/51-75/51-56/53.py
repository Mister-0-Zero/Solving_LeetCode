class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        summ = 0

        for num in nums:
            if summ < 0:
                summ = 0

            summ += num
            res = max(res, summ)

        return res

instance = Solution()
res = instance.maxSubArray([4, -1, 1, -1,  3, -2, 1, -1])
print(res)